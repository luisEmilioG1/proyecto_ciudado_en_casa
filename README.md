# Para desarrolladores

## Instalación
1. Cree el ambiente virtual
```bash
python3 -m venv .venv
```

2. Iniciar ambiente virtual


* En windows
```bash 
.venv\Scripts\Activate.ps1
```
* En linux
```bash 
source .env/bin/activate
```

3. Intalar dependencias
```bash 
pip  install -r requirements.txt
```
4. Crear archivo `.env` de variable de ambiente en la raiz del proyecto y agregar el siguiente contenido
```MD 
HOST=<your db host>
PORT=<your db port>
USER=<your db user>
PASSWORD=<yor db password>
DB=<your database name>
```

5. Cree la base de datos deacuerdo al [DDL](./resources/proySoft2.sql)

6. Iniciar `FastApi` app
```bash 
uvicorn main:app --reload
```
## Uso
* Caso de uso `Consultar signos vitales`

### METHOD
```
    GET
```
### URL
```
    http://127.0.0.1:8000/signo_vital/consultar_signos_vitales
```
### body
```json
    {
        "id": 3,
        "fecha_inicio": "2022-01-01 08:00:00",
        "fecha_fin": "2022-01-02 08:00:0"
    }
```




