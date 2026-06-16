---
source: dify
owner: langgenius
repo: dify
path: docs/es-ES/README.md
url: https://github.com/langgenius/dify/blob/main/docs/es-ES/README.md
---
Dify Cloud ·
  Auto-alojamiento ·
  Documentación ·
  Resumen de las ediciones de Dify

    
        
    
        
    
        
      
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

# 

  

Dify es una plataforma de desarrollo de aplicaciones de LLM de código abierto. Su interfaz intuitiva combina flujo de trabajo de IA, pipeline RAG, capacidades de agente, gestión de modelos, características de observabilidad y más, lo que le permite pasar rápidamente de un prototipo a producción. Aquí hay una lista de las características principales:
 

**1. Flujo de trabajo**:
Construye y prueba potentes flujos de trabajo de IA en un lienzo visual, aprovechando todas las siguientes características y más.

**2. Soporte de modelos completo**:
Integración perfecta con cientos de LLMs propietarios / de código abierto de docenas de proveedores de inferencia y soluciones auto-alojadas, que cubren GPT, Mistral, Llama3 y cualquier modelo compatible con la API de OpenAI. Se puede encontrar una lista completa de proveedores de modelos admitidos aquí.

**3. IDE de prompt**:
Interfaz intuitiva para crear prompts, comparar el rendimiento del modelo y agregar características adicionales como texto a voz a una aplicación basada en chat.

**4. Pipeline RAG**:
Amplias capacidades de RAG que cubren todo, desde la ingestión de documentos hasta la recuperación, con soporte listo para usar para la extracción de texto de PDF, PPT y otros formatos de documento comunes.

**5. Capacidades de agente**:
Puedes definir agentes basados en LLM Function Calling o ReAct, y agregar herramientas preconstruidas o personalizadas para el agente. Dify proporciona más de 50 herramientas integradas para agentes de IA, como Búsqueda de Google, DALL·E, Difusión Estable y WolframAlpha.

**6. LLMOps**:
Supervisa y analiza registros de aplicaciones y rendimiento a lo largo del tiempo. Podrías mejorar continuamente prompts, conjuntos de datos y modelos basados en datos de producción y anotaciones.

**7. Backend como servicio**:
Todas las ofertas de Dify vienen con APIs correspondientes, por lo que podrías integrar Dify sin esfuerzo en tu propia lógica empresarial.

## Usando Dify

- **Nube **
  Hospedamos un servicio Dify Cloud para que cualquiera lo pruebe sin configuración. Proporciona todas las capacidades de la versión autoimplementada e incluye 200 llamadas gratuitas a GPT-4 en el plan sandbox.

- **Auto-alojamiento de Dify Community Edition**
  Pon rápidamente Dify en funcionamiento en tu entorno con esta guía de inicio rápido.
  Usa nuestra documentación para más referencias e instrucciones más detalladas.

- **Dify para Empresas / Organizaciones**
  Proporcionamos características adicionales centradas en la empresa. Envíanos un correo electrónico para discutir las necesidades empresariales. 

  > Para startups y pequeñas empresas que utilizan AWS, echa un vistazo a Dify Premium en AWS Marketplace e impleméntalo en tu propio VPC de AWS con un clic. Es una AMI asequible que ofrece la opción de crear aplicaciones con logotipo y marca personalizados.

## Manteniéndote al tanto

Dale estrella a Dify en GitHub y serás notificado instantáneamente de las nuevas versiones.

## Inicio Rápido

> Antes de instalar Dify, asegúrate de que tu máquina cumpla con los siguientes requisitos mínimos del sistema:
>
> - CPU >= 2 núcleos
> - RAM >= 4GB

La forma más fácil de iniciar el servidor de Dify es ejecutar nuestro archivo docker-compose.yml. Antes de ejecutar el comando de instalación, asegúrate de que Docker y Docker Compose estén instalados en tu máquina:

```bash
cd docker
cp .env.example .env
docker compose up -d
```

Después de ejecutarlo, puedes acceder al panel de control de Dify en tu navegador en http://localhost/install y comenzar el proceso de inicialización.

> Si deseas contribuir a Dify o realizar desarrollo adicional, consulta nuestra guía para implementar desde el código fuente

## Próximos pasos

Si necesita personalizar la configuración, consulte los comentarios en nuestro archivo .env.example y actualice los valores correspondientes en su archivo `.env`. Además, es posible que deba realizar ajustes en el propio archivo `docker-compose.yaml`, como cambiar las versiones de las imágenes, las asignaciones de puertos o los montajes de volúmenes, según su entorno de implementación y requisitos específicos. Después de realizar cualquier cambio, vuelva a ejecutar `docker-compose up -d`. Puede encontrar la lista completa de variables de entorno disponibles aquí.

. Después de realizar los cambios, ejecuta `docker-compose up -d` nuevamente. Puedes ver la lista completa de variables de entorno aquí.

### Monitorización de Métricas con Grafana

Importe el panel a Grafana, utilizando la base de datos PostgreSQL de Dify como fuente de datos, para monitorizar métricas en granularidad de aplicaciones, inquilinos, mensajes y más.

- Panel de Grafana por @bowenliang123

### Implementación con Kubernetes

Si desea configurar una configuración de alta disponibilidad, la comunidad proporciona Gráficos Helm y archivos YAML, a través de los cuales puede desplegar Dify en Kubernetes.

- Gráfico Helm por @LeoQuote
- Gráfico Helm por @BorisPolonsky
- Gráfico Helm por @magicsong
- Ficheros YAML por @Winson-030
- Ficheros YAML por @wyy-holding
- 🚀 ¡NUEVO! Archivos YAML (compatible con Dify v1.6.0) por @Zhoneym

#### Uso de Terraform para el despliegue

Despliega Dify en una plataforma en la nube con un solo clic utilizando terraform

##### Azure Global

- Azure Terraform por @nikawang

##### Google Cloud

- Google Cloud Terraform por @sotazum

#### Usando AWS CDK para el Despliegue

Despliegue Dify en AWS usando CDK

##### AWS

- AWS CDK por @KevinZhao (EKS based)
- AWS CDK por @tmokmss (ECS based)

#### Alibaba Cloud

Alibaba Cloud Computing Nest

#### Alibaba Cloud Data Management

Despliega Dify en Alibaba Cloud con un solo clic con Alibaba Cloud Data Management

#### Uso de Azure Devops Pipeline para implementar en AKS

Implementa Dify en AKS con un clic usando Azure Devops Pipeline Helm Chart by @LeoZhang

## Contribuir

Para aquellos que deseen contribuir con código, consulten nuestra Guía de contribución.
Al mismo tiempo, considera apoyar a Dify compartiéndolo en redes sociales y en eventos y conferencias.

> Estamos buscando colaboradores para ayudar con la traducción de Dify a idiomas que no sean el mandarín o el inglés. Si estás interesado en ayudar, consulta el README de i18n para obtener más información y déjanos un comentario en el canal `global-users` de nuestro Servidor de Comunidad en Discord.

**Contribuidores**

  

## Comunidad y Contacto

- Discusión en GitHub. Lo mejor para: compartir comentarios y hacer preguntas.
- Reporte de problemas en GitHub. Lo mejor para: errores que encuentres usando Dify.AI y propuestas de características. Consulta nuestra Guía de contribución.
- Discord. Lo mejor para: compartir tus aplicaciones y pasar el rato con la comunidad.
- X(Twitter). Lo mejor para: compartir tus aplicaciones y pasar el rato con la comunidad.

## Historial de Estrellas

## Divulgación de Seguridad

Para proteger tu privacidad, evita publicar problemas de seguridad en GitHub. En su lugar, envía tus preguntas a security@dify.ai y te proporcionaremos una respuesta más detallada.

## Licencia

Este repositorio está disponible bajo la Licencia de Código Abierto de Dify, que es esencialmente Apache 2.0 con algunas restricciones adicionales.
