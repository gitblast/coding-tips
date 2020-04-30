## Asennus

Ohjelman saa toimimaan kloonaamalla repositorion, ja ajamalla sen jälkeen juurikansiossa seuraavat komennot:

### Paikallisesti:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

### Herokussa:

```
heroku create
heroku config:set HEROKU=1
heroku addons:add heroku-postgresql:hobby-dev
git remote add heroku <sovelluksen-heroku-url>
git push heroku master
```