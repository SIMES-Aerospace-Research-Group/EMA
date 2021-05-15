# Estación de Monitoreo Ambiental (EMA)
> version 1.0

### EMA, es un dispositivo que permite ver la cantidad de material particulado en el aire, como polvo, humo y gases. Además, también puede medir la temperatura y humedad que hay en el ambiente del mismo lugar en el que se encuentra.

## Módulos utilizados
**`SHARPPM10`** Sensor del material particulado en el aire  

**`MCP3008`** Conversor de señal analógica a digital  

**`HDC1080`** Sensor de temperatura y humedad  

**`DISPLAY LCD 16x02`** Pantalla líquida de 16x02  

**`LED RGB`** L.E.D Red Green Blue  

# Uso

## Instalación
Ingresar al respositorio:
```bash
cd EMA/
```

Instalar librerias requeridas:
```bash
pip3 install -r requirements.txt --force
```

Ejecutar el programa principal:
```bash
python3 main.py
```


