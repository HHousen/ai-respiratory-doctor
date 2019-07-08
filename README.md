![AI Respiratory Doctor Logo](app/static/img/logo_256.png)
# AI Respiratory Doctor
> A flask web app template for use with machine learning projects. Follows best practices such as application factories and Pipfiles.

This template currently contains complete example code to run a fully functional X-Ray diagnosis AI. The model is written with [fast.ai](https://docs.fast.ai/), the backend is [flask](http://flask.pocoo.org/) (and gunicorn server for production), and the frontend uses [Materialize.css](https://materializecss.com/).

Website: <https://ai-respiratory-doctor.herokuapp.com/>

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
* [Python](https://www.python.org/)
* [Pipenv](https://docs.pipenv.org/en/latest/install/#installing-pipenv)
* [Git](https://git-scm.com/)
* [NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

### Installation (Development Setup)

```bash
git clone https://github.com/HHousen/ai-respiratory-doctor.git
cd ai-respiratory-doctor
pipenv install
npm install
cp .env.example .env
source .env
npm start
```

## Project Structure
```bash
ai-respiratory-doctor
├── app
│   ├── admin.py
│   ├── app.db
│   ├── app.py
│   ├── commands.py
│   ├── decorators.py
│   ├── extensions.py
│   ├── forms
│   │   └── user.py
│   ├── logger_setup.py
│   ├── models.py
│   ├── settings.py
│   ├── static
│   │   ├── css
│   │   │   ├── style.css
│   │   │   └── style.css.map
│   │   ├── img
│   │   │   ├── background1.jpg
│   │   │   ├── background2.jpg
│   │   │   ├── background3.jpg
│   │   │   ├── computer-doctor.jpg
│   │   │   ├── error.png
│   │   │   └── favicon.ico
│   │   └── js
│   │       ├── scripts.js
│   │       └── scripts.js.map
│   ├── templates
│   │   ├── admin
│   │   │   └── index.html
│   │   ├── components
│   │   │   ├── footer.html
│   │   │   ├── macros.html
│   │   │   └── nav.html
│   │   ├── email
│   │   │   ├── confirm.html
│   │   │   └── reset.html
│   │   ├── error.html
│   │   ├── index.html
│   │   ├── layout.html
│   │   ├── map.html
│   │   ├── predict.html
│   │   └── user
│   │       ├── account.html
│   │       ├── buy.html
│   │       ├── charge.html
│   │       ├── forgot.html
│   │       ├── reset.html
│   │       ├── signin.html
│   │       ├── signup.html
│   │       └── signup-layout.html
│   ├── toolbox
│   │   └── email.py
│   └── views
│       ├── main.py
│       ├── predict.py
│       └── user.py
├── autoapp.py
├── brunch-config.js
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── models
│   ├── export.pkl
├── package.json
├── package-lock.json
├── Pipfile
├── Pipfile.lock
├── Procfile
├── README.md
├── runtime.txt
├── src
│   ├── assets
│   │   └── img
│   │       ├── background2.jpg
│   │       ├── background3.jpg
│   │       ├── computer-doctor.jpg
│   │       ├── error.png
│   │       └── favicon.ico
│   ├── js
│   │   └── init.js
│   └── sass
│       ├── materialize
│       └── style.scss
└── uploads
```

## Deployment
```
ENV=production
FLASK_ENV=production
```
Push to Heroku with environment variables set. Run command already located in [Procfile](Procfile).
Or use a different service. Run command is ``npm run run-production``

## Meta

Hayden Housen – [haydenhousen.com](https://haydenhousen.com)

Distributed under the MIT license. See the [LICENSE](LICENSE) for more information.

<https://github.com/HHousen>

## Contributing

1. Fork it (<https://github.com/HHousen/ai-respiratory-doctor/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
