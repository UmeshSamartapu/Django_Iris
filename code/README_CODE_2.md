Nice — now we’ll **upgrade your Level 0 project → Level 0.5** 🔥

👉 Goal:

* Save every prediction to **db.sqlite3**
* Show **previous + current predictions** on UI

---

# 🧠 **What We’ll Add**

✅ Store input + result in DB
✅ Show history (like logs)
✅ Keep current prediction

---

# 📁 **1. Update `app/models.py`**

```python
from django.db import models

class IrisPrediction(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()

    prediction = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction} at {self.created_at}"
```

---

# ⚙️ **2. Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 🔥 **3. Update `views.py`**

```python
from django.shortcuts import render
from .ml.predict import predict_iris
from .models import IrisPrediction

def home(request):
    result = None

    if request.method == "POST":
        sepal_length = float(request.POST.get("sepal_length"))
        sepal_width = float(request.POST.get("sepal_width"))
        petal_length = float(request.POST.get("petal_length"))
        petal_width = float(request.POST.get("petal_width"))

        features = [sepal_length, sepal_width, petal_length, petal_width]

        # 🔮 Prediction
        result = predict_iris(features)

        # 💾 Save to DB
        IrisPrediction.objects.create(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width,
            prediction=result
        )

    # 📜 Get all previous records
    history = IrisPrediction.objects.all().order_by('-created_at')

    return render(request, "index.html", {
        "result": result,
        "history": history
    })
```

---

# 🎨 **4. Update `index.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Iris Predictor</title>
</head>
<body>

<h2>Iris Flower Prediction 🌸</h2>

<form method="POST">
    {% csrf_token %}

    <input type="text" name="sepal_length" placeholder="Sepal Length"><br><br>
    <input type="text" name="sepal_width" placeholder="Sepal Width"><br><br>
    <input type="text" name="petal_length" placeholder="Petal Length"><br><br>
    <input type="text" name="petal_width" placeholder="Petal Width"><br><br>

    <button type="submit">Predict</button>
</form>

<hr>

{% if result %}
    <h3>Current Prediction: {{ result }}</h3>
{% endif %}

<hr>

<h3>📜 Previous Predictions</h3>

<table border="1">
    <tr>
        <th>Sepal L</th>
        <th>Sepal W</th>
        <th>Petal L</th>
        <th>Petal W</th>
        <th>Prediction</th>
        <th>Time</th>
    </tr>

    {% for item in history %}
    <tr>
        <td>{{ item.sepal_length }}</td>
        <td>{{ item.sepal_width }}</td>
        <td>{{ item.petal_length }}</td>
        <td>{{ item.petal_width }}</td>
        <td>{{ item.prediction }}</td>
        <td>{{ item.created_at }}</td>
    </tr>
    {% endfor %}
</table>

</body>
</html>
```

---

# 🧠 **Now Flow Becomes**

```text
User Input
   ↓
Prediction (ML)
   ↓
Save to DB (models.py)
   ↓
Fetch all history
   ↓
Show current + past data
```

---

# 🔥 **What You Achieved**

✅ ML + Database integration
✅ Persistent storage
✅ History tracking
✅ Real-world feature (logging predictions)

---

# 🚀 **Next Upgrade Ideas**

👉 Add delete button (clear history)
👉 Add charts (prediction distribution)
👉 Add user login (multi-user history)
👉 Convert to API

---

If you want, next I can show:

👉 **How to view this in Django Admin panel**
👉 OR **Convert this into REST API (like real ML backend)**
