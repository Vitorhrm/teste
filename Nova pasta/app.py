from flask import Flask, render_template

app = Flask(__name__)

videos = [
    {
        "id": 1,
        "title": "Python para iniciantes: do zero ao primeiro projeto",
        "channel": "Code Academy",
        "views": "1,2M visualizações",
        "time": "há 2 dias",
        "duration": "12:45",
        "thumbnail": "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?auto=format&fit=crop&w=900&q=80",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=200&q=80",
    },
    {
        "id": 2,
        "title": "Como criar um layout moderno com HTML e CSS",
        "channel": "Design Lab",
        "views": "845 mil visualizações",
        "time": "há 4 dias",
        "duration": "8:21",
        "thumbnail": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=900&q=80",
        "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=200&q=80",
    },
    {
        "id": 3,
        "title": "Dicas para produtividade no trabalho remoto",
        "channel": "Productivus",
        "views": "630 mil visualizações",
        "time": "há 1 semana",
        "duration": "15:32",
        "thumbnail": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=900&q=80",
        "avatar": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=200&q=80",
    },
    {
        "id": 4,
        "title": "O futuro da IA em aplicações web",
        "channel": "Tech Future",
        "views": "2,4M visualizações",
        "time": "há 3 semanas",
        "duration": "18:10",
        "thumbnail": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=900&q=80",
        "avatar": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=200&q=80",
    },
    {
        "id": 5,
        "title": "Melhores ferramentas para dev em 2026",
        "channel": "Dev Daily",
        "views": "980 mil visualizações",
        "time": "há 5 dias",
        "duration": "10:55",
        "thumbnail": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=900&q=80",
        "avatar": "https://images.unsplash.com/photo-1504593811423-6dd665756598?auto=format&fit=crop&w=200&q=80",
    },
    {
        "id": 6,
        "title": "Como montar uma estratégia de conteúdo digital",
        "channel": "Creator Hub",
        "views": "412 mil visualizações",
        "time": "há 6 dias",
        "duration": "9:40",
        "thumbnail": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=900&q=80",
        "avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=200&q=80",
    },
]


@app.route("/")
def index():
    return render_template("index.html", videos=videos)


@app.route("/video/<int:video_id>")
def video_detail(video_id):
    selected = next((video for video in videos if video["id"] == video_id), videos[0])
    return render_template("video.html", video=selected, videos=videos)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
