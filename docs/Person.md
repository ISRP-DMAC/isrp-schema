
# Class: Person

A simple person

URI: [ex:Person](http://example.org/Person)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PersonCollection]++-%20persons%200..*>[Person&#124;name:string;age:integer%20%3F],[PersonCollection])](https://yuml.me/diagram/nofunky;dir:TB/class/[PersonCollection]++-%20persons%200..*>[Person&#124;name:string;age:integer%20%3F],[PersonCollection])

## Referenced by Class

 *  **None** *[➞persons](personCollection__persons.md)*  <sub>0..\*</sub>  **[Person](Person.md)**

## Attributes


### Own

 * [➞name](person__name.md)  <sub>1..1</sub>
     * Description: The person's full name
     * Range: [String](types/String.md)
 * [➞age](person__age.md)  <sub>0..1</sub>
     * Description: Age in years
     * Range: [Integer](types/Integer.md)
