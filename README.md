📊 A/B Testing y Análisis de Conversión

---

📌 Descripción del Proyecto

Este proyecto simula el análisis de un banco digital que evalúa un rediseño en su proceso de onboarding online.
El objetivo es medir si la nueva interfaz mejora la conversión de usuarios que inician el proceso de alta y reduce errores durante el recorrido digital.
La conversión se define como la finalización completa del proceso, mientras que el error representa abandonos o fallos en pasos críticos del funnel.

Análisis end-to-end de un experimento A/B para evaluar el impacto de un nuevo diseño de interfaz sobre la conversión de usuarios.

El proyecto incluye:

- Limpieza e integración de datos


- Perfilado de clientes


- Análisis de funnel


- Test estadístico


- Evaluación de impacto en negocio


-Dashboard ejecutivo en Tableau


---


🎯 Objetivo

Determinar si el nuevo diseño:


- Incrementa la tasa de conversión


- Reduce la tasa de error


- Mejora la eficiencia del recorrido del usuario


---


📈 Resultados Principales

Métrica          Control	        Test	        Impacto


Conversión	     65.59%	          69.29%	      +3.7 p.p.


Error	           34.41%	          30.71%	      −3.7 p.p.


Pasos promedio	  4.18	           4.04	     No significativo



Nivel de significancia:       α = 0.05


Test aplicado:             Z-test de proporciones


---


Conclusión



El nuevo diseño mejora significativamente la conversión y reduce errores.
Sin embargo, no alcanza el umbral económico definido (+5%) para justificar su implementación inmediata.
Se define un umbral mínimo de +5% de mejora en conversión para cubrir costes de implementación, riesgo operacional y asegurar un retorno de inversión positivo en el corto plazo.



---


🧱 Estructura del Proyecto
---------------------------
notebooks/
data/
src/
dashboards/
---------------------------



El flujo incluye preparación de datos, integración, análisis exploratorio, funnel, segmentación y A/B test final.


---


🛠 Tecnologías

Python · Pandas · NumPy · SciPy · Statsmodels · Matplotlib · Tableau



--- 



🔎 Lo que demuestra este proyecto

Construcción de pipeline de datos

Diseño y validación de experimentos

Análisis de comportamiento de clientes

Enfoque orientado a decisión de negocio



---


🔬 Validación Estadística

- Se validó el balance del experimento entre grupo Control y Test.

- Se aplicó un Z-test de proporciones para comparar tasas de conversión.

- Se verificaron supuestos de tamaño muestral suficiente para aproximación normal.

- Se calculó intervalo de confianza del 95% para la diferencia de proporciones.

- Nivel de significancia: α = 0.05.
