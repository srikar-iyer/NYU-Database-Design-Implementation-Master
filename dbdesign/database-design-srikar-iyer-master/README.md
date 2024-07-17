# Data Normalization and Entity-Relationship Diagramming

The goal of this project is to convert a table in a database in 1st Normal Form to 4th Normal Form. The table in question is shown below : 

| assignment_id | student_id | due_date | professor | assignment_topic                | classroom | grade | relevant_reading    | professor_email   |
| :------------ | :--------- | :------- | :-------- | :------------------------------ | :-------- | :---- | :------------------ | :---------------- |
| 1             | 1          | 23.02.21 | Melvin    | Data normalization              | WWH 101   | 80    | Deumlich Chapter 3  | l.melvin@foo.edu  |
| 2             | 7          | 18.11.21 | Logston   | Single table queries            | 60FA 314  | 25    | Dümmlers Chapter 11 | e.logston@foo.edu |
| 1             | 4          | 23.02.21 | Melvin    | Data normalization              | WWH 101   | 75    | Deumlich Chapter 3  | l.melvin@foo.edu  |
| 5             | 2          | 05.05.21 | Logston   | Python and pandas               | 60FA 314  | 92    | Dümmlers Chapter 14 | e.logston@foo.edu |
| 4             | 2          | 04.07.21 | Nevarez   | Spreadsheet aggregate functions | WWH 201   | 65    | Zehnder Page 87     | i.nevarez@foo.edu |
| ...           | ...        | ...      | ...       | ...                             | ...       | ...   | ...                 | ...               |

## Explaining Original Table (1st Normal Form)

This table represents information about students' grades in courses at a university.

Specifically, the columns included are: assignment_id, student_id, due_date, professor,  assignment_topic, classroom, grade, relevant_reading, and professor_email.

While this does provide information regarding the students, assignments, and course structure, it does not acknowledge dependencies the data can have. Being in 1st normal form, all records in the table have the same number of fields and a consistent fixed schema (rows, columns). Also, all values recorded are singular (only 1 value per field). 

It does not follow 2nd, 3rd, or 4th normal forms since fields in the table are dependent on each other, each entity is not uniquely identifiable by a unique primary key, and even then, there exists many multi-valued facts about some entities, such as assignments having relevant readings and due dates.

## Explaining the Modification of the Table to 2nd, 3rd, 4th Normal Forms

To convert a table in 1st normal form to 4th normal form, the final result should also follow the requirements of 2nd and 3rd normal forms. I directly executed the modifications to 2nd, 3rd, and 4th normal form concurrently making the E.R. diagram, but will explain mentally how I added the characteristics of 2nd, 3rd, and 4th normal forms in order.

### Filling in gaps 

So, the main change here would be to add vital entities and attributes missing that are required for the data to make sense. This is partially because dependencies between 2 entities in the table are usually caused by a different entity not included (i.e. classroom and professor are both related to each course section). Also, there are entity-less attributes that require entities (i.e. student_id is an attribute of the unmentioned entity student). The complete list of entities is course, professor, assignment, reading, classroom, section, and student, most of which were ignored by the original table but vital to include in order to make unambiguous any relevant dependancies.

### 2nd and 3rd normal forms

The new conditions imposed by this restriction that must be met are that any non-key field must provide information about the specific, unique, and complete entity identified by the primary key, and that any non-key field must be a fact about other non-key fields. So, each entity would be placed into its own table along with a corresponding primary key, corresponding attributes, and necessary foreign keys if the entity has a relationship with other entities. This was according to the logic of the known dependencies. So for example, we know that, "professors give readings that are relevant and helpful to a given assignment". The reading table, accordingly, includes a reading_id primary key, given attribute relevant_reading, and foreign key assignment_id. This foreign key is because each assignment can have multiple readings, creating a relation between the two entities. Hence, this setup satisfies 2nd and 3rd normal forms.

### 4th normal form

Given the previous results (satisfying 3rd normal form), to satisfy 4th normal form, it is just required to not contain more than one independent multi-valued fact about an entity. Here, splitting tables helps when the cardinality between the entities is one to one or one to many (or many to one, but implied). For instance, because each professor might teach multiple sections of the same course, assigning a foreign key, professor_id, to the sections entity covers all of the sections that each professor might teach. However, multiple students might have multiple assignments, in the many to many case. Then, it might be harder to ensure reduction of redundancy and independence of entities, but using join table between two entities, we can create 2 one to many relationships. 

## The Final Tables in 4th normal form

Primary keys are italicized, and foreign keys also have a "F" subscript.

### Course

| _course_id_ | course_name |
| :---------- | :---------- |
| 1           | DB Design   |
| 2           | Calculus I  |

### Professor 
| _professor_id_ | professor_name | professor_email   |
| :------------- | :------------- | :---------------- |
| 1              | Melvin         | l.melvin@foo.edu  |
| 2              | Logston        | e.logston@foo.edu |
| 3              | Nevarez        | i.nevarez@foo.edu |


### Assignment
| _assignment_id_ | assignment_topic                |
| :-------------- | :------------------------------ |
| 1               | Data normalization              |
| 2               | Python and pandas               |
| 3               | Spreadsheet aggregate functions |
| 4               | Single table queries            |


### Reading
| _reading_id_ | relevant_reading    | _assignment_id_<sub>F</sub> |
| :----------- | :------------------ | :-------------------------- |
| 1            | Deumlich Chapter 3  | 1                           |
| 2            | Deumlich Chapter 11 | 4                           |
| 3            | Deumlich Chapter 14 | 2                           |
| 4            | Zehnder Page 87     | 3                           | 

### Classroom
| _classroom_id_ | classroom_name |
| :------------- | :------------- |
| 1              | WWH 101        |
| 2              | 60FA 314       |
| 3              | WWH 101        |

### Section
| _section_id_ | section_name | _assignment_id_<sub>F</sub> | _classroom_id_<sub>F</sub> | _professor_id_<sub>F</sub> | _course_id_<sub>F</sub> |
| :----------- | :----------- | :-------------------------- | :------------------------- | :------------------------- | :---------------------- |
| 1            | DN - Sec A   | 1                           | 1                          | 1                          | 1                       | 
| 2            | STQ-Sec A    | 4                           | 2                          | 2                          | 1                       | 
| 3            | P&P-Sec A    | 2                           | 2                          | 2                          | 1                       | 
| 4            | SAF-Sec A    | 3                           | 3                          | 3                          | 1                       | 

### Student
| _student_id_ | student_name | 
| :----------- | :----------- |
| 1            | Sebchoof     | 
| 2            | Geranium     | 
| 3            | Crainer      | 
| 4            | Potatoe      | 
| 5            | NeymarJr     | 
| 6            | Cleveland    | 
| 7            | Stewie       | 




### Student_assignment
| _stu_assign_id_ | _assignment_id_<sub>F</sub> | _student_id_<sub>F</sub> | Grade | 
| :-------------- | :-------------------------- | :----------------------- | :---- |
| 1               | 1                           | 1                        | 80    |
| 2               | 7                           | 4                        | 25    |
| 3               | 4                           | 1                        | 75    |
| 4               | 2                           | 2                        | 92    |
| 5               | 2                           | 3                        | 65    |



### Student_section
| _stu_sec_id_ | _student_id_<sub>F</sub> | _section_id_<sub>F</sub> |
| :----------- | :----------------------- | :----------------------- |
| 1            | 1                        | 1                        |
| 2            | 7                        | 2                        |
| 3            | 4                        | 1                        |
| 4            | 2                        | 3                        |
| 5            | 2                        | 4                        |

### Section_assignment
| _sec_assign_id_ | _assignment_id_<sub>F</sub> | _section_id_<sub>F</sub> | Due_date   |
| :-------------- | :-------------------------- | :----------------------- | :--------- |
| 1               | 1                           | 1                        | 2/23/2021  |
| 2               | 2                           | 4                        | 11/18/2021 |
| 3               | 3                           | 2                        | 5/5/2021   |
| 4               | 4                           | 3                        | 7/4/2021   |
## The ER Diagram used to organize and relate entities and their attributes


![sample.svg](https://github.com/dbdesign-assignments-spring2023/database-design-srikar-iyer/blob/b7595989006b14f104588c618cfca567ac7ebb91/images/datasciencehw.drawio.svg)

