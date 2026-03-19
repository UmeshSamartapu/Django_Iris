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