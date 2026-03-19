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