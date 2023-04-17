from django.http import HttpRequest,HttpResponse


def name(request: HttpRequest)->HttpResponse:
    if request.method=="POST":
        name = request.POST.get("name","")
        age = int(request.POST.get("age", "0"))
        return HttpResponse(f"""
        Thanks,{name}!<br>
        You are {age} years old
        """)
    return HttpResponse("""
    <form method = "POST">
    <label for = "name">What is your name?</label>
    <input id="name" name ="name" value = "Dastan"><br>
    <label for = "age">What is your age?</label>
    <input id="age";name="age"; type ="number"; value = "19"><br>
    <button type="submit">OK</button>
    </form>
    """)


