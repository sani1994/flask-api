This project is built in Python and flask framework<br />
**System Requirements:**
    Python=3.10.0<br />
    click==8.1.3<br />
    Flask==2.2.3<br />
    itsdangerous==2.1.2<br />
    Jinja2==3.1.2<br />
    MarkupSafe==2.1.2<br />
    psycopg2-binary==2.9.5<br />
    Werkzeug==2.2.3<br />

**Run**:<br/>
    **Local run:**<br/>
        * clone project<br />
        * make sure the database docker is up and running in localhost<br />
        * execute `run.sh` if shows permission denied please give execute permission to `run.sh`. ex:`chmod +x run.sh` [it will create virtual environment and install the requirements]
    <br/>
    **Docker run:** <br/>
        * clone project.
        * go to `docker-files` directory. [cd docker-files]
        * docker-compose build
        * dcoker-compose up
    