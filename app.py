from flask import Flask, request, render_template
import pymongo


myclient = pymongo.MongoClient() #add your own
nyolcb = [3563, 3659, 7552, 8738, 7729, 8516, 7680, 7857, 2804, 8565, 7768, 7541, 3076, 8218, 7963, 5377]
nyolca = []
hetb = []
heta = []
hata = []
hatb = []
otb = []
ota = []

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    if int(text) in nyolcb:
        nyolcb.remove(int(text))
        return app.redirect('/tTzYawcpDWsqpvqWglxoCQ')
    else:
        if int(text) in nyolca:
            nyolcb.remove(int(text))
            return app.redirect('/rgWIkYv6plKHAQcwpvUrPA')
        else:
            if int(text) in hetb:
                hetb.remove(int(text))
                return app.redirect('/rubMvPgZgDCdApyKbGEw')
            else:
                if int(text) in heta:
                    heta.remove(int(text))
                    return app.redirect('/aZD7j4qU1Y9anpmyPVj65w')
                else:
                    if int(text) in hatb:
                        hatb.remove(int(text))
                        return app.redirect('/5LmLPRYzwTuOfJOjdDge8A')
                    else:
                        if int(text) in hata:
                            hata.remove(int(text))
                            return app.redirect('/PYhe0ABRJBY0d50R2MZrLQ')
                        else:
                            if int(text) in otb:
                                otb.remove(int(text))
                                return app.redirect('/uKRdeS9axqCdVDJHtlym9g')
                            else:
                                if int(text) in ota:
                                    ota.remove(int(text))
                                    return app.redirect('/RS6pwjkpmz6Qp7X1rHIxVw')
                                else:
                                    return app.redirect('/')



@app.route('/tTzYawcpDWsqpvqWglxoCQ')
def nyolcbe():
    return render_template('nyolcb.html')
@app.route('/rgWIkYv6plKHAQcwpvUrPA')
def nyolcaa():
    return render_template('nyolca.html')
@app.route('/rubMvPgZgDCdApyKbGEw')
def hetbe():
    return render_template('hetb.html')
@app.route('/aZD7j4qU1Y9anpmyPVj65w')
def hetaa():
    return render_template('heta.html')
@app.route('/5LmLPRYzwTuOfJOjdDge8A')
def hatbe():
    return render_template('hatb.html')
@app.route('/PYhe0ABRJBY0d50R2MZrLQ')
def hataa():
    return render_template('hata.html')
@app.route('/uKRdeS9axqCdVDJHtlym9g')
def otbe():
    return render_template('otb.html')
@app.route('/RS6pwjkpmz6Qp7X1rHIxVw')
def otaa():
    return render_template('ota.html')



@app.route('/button_pressed', methods=['POST'])
def button_pressed():
    global button_press
    button_press = request.form['button']
    
    if button_press == "8B":
        mydb = myclient["mydatabase"]
        mycol = mydb["nyolcB"]


        x = mycol.find_one()

        print(x["szam"])

        mydict = { "$set": {"szam":int(x["szam"]) + 1} }

        mycol.update_one(x, mydict)
        return render_template('thanks.html')
    else:
        if button_press == "8A":
            mydb = myclient["mydatabase"]
            mycol = mydb["nyolcA"]


            x = mycol.find_one()

            print(x["szam"])

            mydict = { "$set": {"szam":int(x["szam"]) + 1} }

            mycol.update_one(x, mydict)
            return render_template('thanks.html')
        else:
            if button_press == "7B":
                mydb = myclient["mydatabase"]
                mycol = mydb["hetB"]


                x = mycol.find_one()

                print(x["szam"])

                mydict = { "$set": {"szam":int(x["szam"]) + 1} }

                mycol.update_one(x, mydict)
                return render_template('thanks.html')
            else:
                if button_press == "7A":
                    mydb = myclient["mydatabase"]
                    mycol = mydb["hetA"]


                    x = mycol.find_one()

                    print(x["szam"])

                    mydict = { "$set": {"szam":int(x["szam"]) + 1} }

                    mycol.update_one(x, mydict)
                    return render_template('thanks.html')
                else:
                    if button_press == "6B":
                        mydb = myclient["mydatabase"]
                        mycol = mydb["hatB"]


                        x = mycol.find_one()

                        print(x["szam"])

                        mydict = { "$set": {"szam":int(x["szam"]) + 1} }

                        mycol.update_one(x, mydict)
                        return render_template('thanks.html')
                    else:
                        if button_press == "6A":
                            mydb = myclient["mydatabase"]
                            mycol = mydb["hatA"]


                            x = mycol.find_one()

                            print(x["szam"])

                            mydict = { "$set": {"szam":int(x["szam"]) + 1} }

                            mycol.update_one(x, mydict)
                            return render_template('thanks.html')
                        else:
                            if button_press == "5B":
                                mydb = myclient["mydatabase"]
                                mycol = mydb["otB"]


                                x = mycol.find_one()

                                print(x["szam"])

                                mydict = { "$set": {"szam":int(x["szam"]) + 1} }

                                mycol.update_one(x, mydict)
                                return render_template('thanks.html')
                            else:
                                if button_press == "5A":
                                    mydb = myclient["mydatabase"]
                                    mycol = mydb["otA"]


                                    x = mycol.find_one()

                                    print(x["szam"])

                                    mydict = { "$set": {"szam":int(x["szam"]) + 1} }

                                    mycol.update_one(x, mydict)
                                    return render_template('thanks.html')
                    
