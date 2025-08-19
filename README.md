# Proyecto Kenpo Avatar

Plataforma de generación de animaciones biomecánicas para Kenpo Karate, asistida por IA. Este proyecto es liderado por Sergio Valenzuela con la asistencia de un experto en IA.

## Visión General

Este proyecto utiliza un flujo de trabajo "Video-a-Video" para transformar grabaciones de técnicas de artes marciales en animaciones de avatares 3D estilizados, preservando la fidelidad biomecánica del movimiento original.

## Arquitectura del Sistema

A continuación se presenta el diagrama de arquitectura conceptual de la aplicación.

```mermaid
graph TD
    subgraph "Usuario"
        A[Practicante/Instructor]
    end

    subgraph "Plataforma Kenpo Avatar (Vercel)"
        B{Frontend (React & TypeScript)}
        C{Backend (Django & DRF)}
    end

    subgraph "Servicios de IA Externos"
        D[Motor de Análisis de Movimiento (MediaPipe)]
        E[Motor de Renderizado de Video (Sora/VEO3)]
    end

    A -- Carga Video/Prompt --> B;
    B -- Envía Solicitud --> C;
    C -- Analiza Video --> D;
    C -- Envía Tarea de Renderizado --> E;
    E -- Devuelve Video Final --> C;
    C -- Envía Resultado --> B;
    B -- Muestra Animación --> A;
