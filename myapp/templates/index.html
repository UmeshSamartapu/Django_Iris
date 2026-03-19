<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Iris Predictor 🌸</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gradient-to-br from-indigo-100 to-purple-200 min-h-screen p-6">

<div class="max-w-4xl mx-auto">

    <!-- Header -->
    <h1 class="text-4xl font-bold text-center text-gray-800 mb-8">
        🌸 Iris Flower Predictor
    </h1>

    <!-- Form Card -->
    <div class="bg-white shadow-xl rounded-2xl p-6 mb-8">
        <form method="POST" class="grid grid-cols-1 md:grid-cols-2 gap-4">
            {% csrf_token %}

            <input type="text" name="sepal_length" placeholder="Sepal Length"
                   class="p-3 border rounded-xl focus:ring-2 focus:ring-indigo-400 outline-none">

            <input type="text" name="sepal_width" placeholder="Sepal Width"
                   class="p-3 border rounded-xl focus:ring-2 focus:ring-indigo-400 outline-none">

            <input type="text" name="petal_length" placeholder="Petal Length"
                   class="p-3 border rounded-xl focus:ring-2 focus:ring-indigo-400 outline-none">

            <input type="text" name="petal_width" placeholder="Petal Width"
                   class="p-3 border rounded-xl focus:ring-2 focus:ring-indigo-400 outline-none">

            <button type="submit"
                    class="col-span-1 md:col-span-2 bg-indigo-500 text-white py-3 rounded-xl hover:bg-indigo-600 transition duration-300">
                🔍 Predict
            </button>
        </form>
    </div>

    <!-- Result -->
    {% if result %}
    <div class="bg-green-100 border-l-4 border-green-500 p-4 rounded-xl mb-6">
        <h3 class="text-lg font-semibold text-green-800">
            ✅ Prediction: {{ result }}
        </h3>
    </div>
    {% endif %}

    <!-- History Table -->
    <div class="bg-white shadow-xl rounded-2xl p-6">
        <h3 class="text-xl font-semibold mb-4 text-gray-700">
            📜 Prediction History
        </h3>

        <div class="overflow-x-auto">
            <table class="w-full text-sm text-left border-collapse">
                <thead>
                    <tr class="bg-indigo-500 text-white">
                        <th class="p-3">Sepal L</th>
                        <th class="p-3">Sepal W</th>
                        <th class="p-3">Petal L</th>
                        <th class="p-3">Petal W</th>
                        <th class="p-3">Prediction</th>
                        <th class="p-3">Time</th>
                    </tr>
                </thead>

                <tbody>
                    {% for item in history %}
                    <tr class="border-b hover:bg-gray-100 transition">
                        <td class="p-3">{{ item.sepal_length }}</td>
                        <td class="p-3">{{ item.sepal_width }}</td>
                        <td class="p-3">{{ item.petal_length }}</td>
                        <td class="p-3">{{ item.petal_width }}</td>
                        <td class="p-3 font-semibold text-indigo-600">{{ item.prediction }}</td>
                        <td class="p-3 text-gray-500">{{ item.created_at }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

</div>

</body>
</html>