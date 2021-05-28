# Estación de Monitoreo Ambiental (EMA) - debug version
> version 1.0

### EMA, es un dispositivo que permite medir la cantidad de material particulado en el aire, como polvo, humo y gases. Además, también puede medir la temperatura y humedad que hay en el ambiente del mismo lugar en el que se encuentra, graficándolo constantemente en su pantalla LCD y Dashboard.

## Módulos utilizados
**`SHARPPM10`** Sensor de material particulado en el aire  

**`MCP3008`** Conversor de señal analógica a digital  

**`HDC1080`** Sensor de temperatura y humedad  

**`DISPLAY LCD 16x02`** Pantalla líquida de 16x02

**`LED RGB`** L.E.D Red Green Blue  

## Instalación
Activar interfaces I2C y SPI:
```bash
sudo raspi-config
```

Clonar el repositorio de GitHub:
```bash
git clone https://github.com/CON-CIENCIA-CL/EMA.git
```

Ingresar al repositorio:
```bash
cd EMA/
```

Ejecutar script que instala los packetes necesarios automaticamente:
```bash
python3 setup.py
```

Reiniciar dispositivo Pi para efectuar cambios de interfaces y packetes:
```bash
sudo reboot
```
