from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Chemical Equipment Parameter Visualizer</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f4f6f8;
                        text-align: center;
                        padding-top: 80px;
                    }
                    .box {
                        background: white;
                        display: inline-block;
                        padding: 30px 40px;
                        border-radius: 8px;
                        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    }
                </style>
            </head>
            <body>
                <div class="box">
                    <h1>Chemical Equipment Parameter Visualizer</h1>
                    <p>Django REST Backend is running successfully.</p>
                    <p>Use <b>/api/</b> endpoints to access data.</p>
                </div>
            </body>
        </html>
    """)