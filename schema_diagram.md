# Schema Diagram

```mermaid
erDiagram
  Person {
    string name
    integer age
  }
  
  PersonCollection {
    Person[] persons
  }

  PersonCollection ||--|{ Person : contains

  %% Optional clickable links to GitHub documentation
  click Person "https://github.com/ISRP-DMAC/isrp-schema#person" "Person class docs"
  click PersonCollection "https://github.com/ISRP-DMAC/isrp-schema#personcollection" "Collection docs"
