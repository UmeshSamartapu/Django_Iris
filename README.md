

# 📁 **Project Structure**

```
deep_learning_project/
│
├── manage.py
├── requirements.txt
│
├── deep_learning_project/        # Main project config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app/                          # Main ML app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                 # DB (optional)
│   ├── views.py                  # Logic (IMPORTANT)
│   ├── urls.py
│   ├── tests.py
│
│   ├── ml/                       # 🔥 ML/DL Logic Folder
│   │   ├── __init__.py
│   │   ├── model_loader.py       # Load model once
│   │   ├── predict.py            # Prediction logic
│   │   └── preprocess.py         # Image preprocessing
│
│   ├── templates/
│   │   └── index.html            # Upload UI
│
│   └── static/
│       └── style.css
│
├── media/                        # Uploaded files
│   └── uploads/
│
└── model/                        # 🔥 Saved models
    └── model.h5
```

---


"# Django_Iris" 
