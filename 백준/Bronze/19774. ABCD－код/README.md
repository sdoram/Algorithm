# [Bronze III] ABCD-код - 19774 

[문제 링크](https://www.acmicpc.net/problem/19774) 

### 성능 요약

메모리: 32412 KB, 시간: 584 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2025년 7월 21일 21:07:53

### 문제 설명

<p>Вася часто ходит в гости к Пете. Для того, чтобы попасть к Пете во двор, надо ввести код, состоящий из четырех цифр. Обычно друзья ходили вместе, но в этот раз Вася пришел один, а Петя ждет его у себя.</p>

<p>Вася не помнит код, но у него есть несколько вариантов. Кроме того, Васе почему-то запомнился факт, что квадрат числа, составленного из первых двух цифр кода, в сумме с квадратом числа, состоящего из последних двух цифр кода, имеет при делении на семь остаток один. То есть, если код представляет собой <<$ABCD$>>, где <<$A$>>, <<$B$>>, <<$C$>>, <<$D$>> --- некоторые цифры, тогда $AB^2 + CD^2$ имеет остаток 1 при делении на 7. Например, код 2843, является одним из возможных кодов, поскольку $28^2 + 43^2=2633 = 376 \cdot 7 + 1$, а 8243 --- нет, поскольку $82^2 + 43^2=8573 = 1224 \cdot 7 + 5$.</p>

<p>У Васи есть несколько вариантов того, каким может быть код. Помогите ему определить, какие из вариантов могут быть кодом от входа в Петин двор.</p>

### 입력 

 <p>В первой строке входного файла находится число $t$ ($1 \le t \le 10\,000$) --- число вариантов кода, которые помнит Вася. В следующих $t$ строках содержится по четыре цифры --- варианты кода.</p>

### 출력 

 <p>В выходной файл выведите $t$ строк. В $i$-й строке выведете <<<code>YES</code>>>, если $i$-й код может быть кодом для входа в Петин двор, иначе выведете <<<code>NO</code>>>,</p>

