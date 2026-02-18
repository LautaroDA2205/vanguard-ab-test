📊 A/B Testing y Análisis de Conversión
📌 Descripción del Proyecto

Análisis end-to-end de un experimento A/B para evaluar el impacto de un nuevo diseño de interfaz sobre la conversión de usuarios.

El proyecto incluye:

- Limpieza e integración de datos

- Perfilado de clientes

- Análisis de funnel

- Test estadístico

- Evaluación de impacto en negocio

-Dashboard ejecutivo en Tableau


🎯 Objetivo

Determinar si el nuevo diseño:

- Incrementa la tasa de conversión

- Reduce la tasa de error

- Mejora la eficiencia del recorrido del usuario


📈 Resultados Principales

Métrica	Control	Test	Impacto

Conversión	              65.59%	69.29%	+3.7 p.p.
Error	                    34.41%	30.71%	−3.7 p.p.
Pasos promedio	          4.18	4.04	No significativo

Nivel de significancia:       α = 0.05
Test aplicado:             Z-test de proporciones

Conclusión

El nuevo diseño mejora significativamente la conversión y reduce errores.
Sin embargo, no alcanza el umbral económico definido (+5%) para justificar su implementación inmediata.


🧱 Estructura del Proyecto
---------------------------
notebooks/
data/
src/
dashboards/
---------------------------

El flujo incluye preparación de datos, integración, análisis exploratorio, funnel, segmentación y A/B test final.


🛠 Tecnologías

Python · Pandas · NumPy · SciPy · Statsmodels · Matplotlib · Tableau


🔎 Lo que demuestra este proyecto

Construcción de pipeline de datos

Diseño y validación de experimentos

Análisis de comportamiento de clientes

Enfoque orientado a decisión de negocio