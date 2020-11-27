# Jimbru

Jimbru is an Privacy Oriented web analytics Server which is built with FastAPI and Deta Base as DB.

> Jimbru is heavily inspired by [Shynet](https://github.com/milesmcc/shynet) which is also an Analytics server built with Django.


**Not for Production Level use. It's hacky to the core. I made it for a Personal Use and doesn't have any fancy features.**


## Features

- Lightweight
- Privacy Oriented
- Easily Deployable (on deta.sh)
- 6 lines of JS code gets the current URL, referrer and load time.
- Charts with [Frappe Charts](https://frappe.io/charts) 📊
- Jinja2 Templating and Tailwind CSS for Frontend
- Cookie based Authentication
- User OS and device from `user-agent` header
- user location and network from user ip header

## Not Included Features
- Caching
- Bounce rate
- Session Time
- Unique Hits

## Demo

![Demo Gif](https://user-images.githubusercontent.com/40897573/99864902-1fb1c980-2bcc-11eb-81e6-49380d36d263.gif)

## Deploying

Before deploying you need to get some Credentials

### Prep Work
- Signup for an account in https://deta.sh
- Create a new Project 
- Get the Project Key and save it in the `.env` file as below
- [Install](https://docs.deta.sh/docs/cli/install) the Deta cli. This is for deploying to Deta.
- Create a `.env` file inside the `app/routes` directory with the following keys

    ```env
    TITLE=<title of the site>
    DOMAIN=<domain of the deployed server>
    PKEY=<Deta Project Key>
    PNAME=<Deta Base DB Name>
    SECRET_JWT=<Secret for JWT. Get than with→ import os; print(os.urandom(24).hex())>
    USERNAME=<username for authenticating>
    PASSWORD=<password for authenticating>
    ```

> The `PNAME` can be anything.

---

1. Fork/Clone this Repository
2. You can run the code locally by installing the dependencies inside the `app` directory and running `uvicorn main:app --reload` inside the `app` directory.
3. Inside the `app` directory you can create a new [Micro](https://docs.deta.sh/docs/micros/about) with `$ deta new`. This will create a new Micro. You will get the domian from the output of the command. Save that domain in the `DOMAIN` key in the `.env` file, without a trailing `/`.
4. Run `$ deta update -e routes/.env` to update the environment variables in the micro.
5. Run `$ deta deploy` inside the app directory and the code will be deployed.
6. Profit

---

## Usage

Add a `<script>` tag for the site

```html
<script src="https://<DOMAIN>/a.js" type="text/javascript"></script>
```

## TODO

- [ ] Caching
- [ ] Better Auth
- [ ] Session Time

## LICENSE

**MIT**

## Contributors

- [@akhilmhdh](https://github.com/akhilmhdh)
