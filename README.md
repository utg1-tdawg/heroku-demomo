## Initial set-up
```
heroku login 
heroku create heroku-demomo
cd client
npm run build
cd ..
git push heroku main
```

## Set environment variables
```
heroku config:set FLASK_DEMOMO_VAR="demomo"
```

## Reflect changes
```
npm run build # if necessary
git commit -m "changes"
git push heroku main
```

## Comments
Without proxying to flask backend, we have to hardcode server's domain (see `fetch`) \
This makes it troublesome to switch from development to production, vice versa
