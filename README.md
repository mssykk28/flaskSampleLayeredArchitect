# flaskSampleLayeredArchitect

## 参照条件
```
    参照OK;
            presentation-->application;
            ex)controller-->service;
            
            application-->infrastructure;
            ex)service-->repository;
    参照NG;
            application-->presentation;
            ex)service-->controller;
            
            presentation-->infrastructure;
            ex)controller-->repository;
```