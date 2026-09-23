### Linting e estilo

O projeto utiliza **Pylint** para verificar qualidade, estilo e possíveis problemas no código Python.

As principais convenções são:
    * utilizar "chore:" antes do inicio do commit 
    * Utilizar **Python 3.14** como referência.
    * Variáveis, argumentos, atributos, funções, métodos e módulos devem seguir **`snake_case`**.
    * Classes devem seguir **`PascalCase`**.
    * Constantes devem seguir **`UPPER_CASE`**.
    * Utilizar **4 espaços** para indentação.
    * O limite de uma linha é de **200 caracteres**.
    * Evitar funções e métodos excessivamente complexos ou extensos, respeitando os limites definidos na configuração do Pylint.
    * Evitar o uso de exceções genéricas (`Exception` e `BaseException`) quando uma exceção mais específica puder ser utilizada.
    * Nomes genéricos como `foo`, `bar`, `baz`, `toto`, `tutu` e `tata` não devem ser utilizados.
    * O código deve respeitar as verificações e mensagens habilitadas pelo Pylint.
    * A análise utiliza apenas determinados níveis de confiança definidos na configuração.
    * O projeto possui um **score mínimo de 9/10** no Pylint. Contribuições que resultem em uma nota inferior a esse limite devem ser corrigidas antes de serem integradas.
