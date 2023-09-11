## Habilidades exercitadas:

Neste projeto fui responsável por construir testes para classes já implementadas, implementar uma nova classe para mapear os pratos e suas respectivas receitas (ingredientes e quantidades), e também implementar uma classe que gerará os cardápios que devem ser mostrados para as pessoas que frequentam o estabelecimento e outra que fará a gestão de estoque dos ingredientes. Isso foi feito por meio de:

- Praticar o conceito de Hashmaps através das estruturas de dados Dict e Set do Python;
- Praticar os conhecimentos de testes de software;
- Praticar os conhecimentos de orientação a objetos.

# Requisitos:

## 1 - Testando classes já implementadas parte 1

> Implementar testes para a classe `Ingredient`, que se encontra no módulo `src/models/ingredient.py`.

A primeira das classes implementadas é a `Ingredient` que representa os ingredientes, um objeto desta classe contém o nome e restrições alimentares do ingrediente como atributos.

A classe já possui alguns métodos mágicos já implementados que garantem funcionalidades específicas. Os métodos já implementados são: `__repr__`, `__eq__` e `__hash__`.

### Implementação

Escrever os testes para a classe `Ingredient` no arquivo `tests/ingredient/test_ingredient.py`. Seus testes devem garantir que:

- a classe pode ser instanciada corretamente de acordo com a assinatura esperada;
- o atributo conjunto `restrictions` é populado como esperado;
- o método mágico `__repr__` funcione como esperado;
- o método mágico `__eq__` funcione como esperado;
- o método mágico `__hash__` funcione como esperado.

## 2 - Testando classes já implementadas parte 2

> Implementar testes para a classe `Dish`, que se encontra no módulo `src/models/dish.py`.

A outra classe a ser testada é a `Dish`, que representa um prato do cardápio. Uma instância desta classe possui atributos representando o nome, o preço e a receita do prato.

Tal como a classe `Ingredient`, a classe `Dish` já possui alguns métodos já implementados: `add_ingredient_dependency`, `get_restrictions`, `get_ingredients`, `__repr__`, `__eq__` e `__hash__`.

### Implementação

Escrever os testes para a classe `Dish` no arquivo `tests/dish/test_dish.py`. Seus testes devem garantir que:

- a classe pode ser instanciada corretamente de acordo com a assinatura esperada;
- os métodos da classe, inclusive os métodos mágicos, funcionem como esperado;
- o dicionário de receita do prato devolve a quantidade correta de um ingrediente;
- são levantados erros ao criar pratos inválidos;

## 3 - Mapeamento Pratos <> Ingredientes

> Implementar a classe `MenuData` que fará todo o mapeamento de pratos e ingredientes baseado nos arquivo csv disponibilizado. Ela se encontra no módulo `src/services/menu_data.py`.

Hoje, a gestão de pratos e receitas do Restaurante é feita por meio de um arquivo csv. Em cada linha deste arquivo há o nome do prato, seu preço no cardápio, um dos ingredientes que o compõe e a quantidade necessária daquele ingrediente na receita. Essa organização faz com que um único prato seja representado por múltiplas linhas no mesmo arquivo.

A tarefa é implementar uma classe que fará a leitura do arquivo csv mencionado e fará o relacionamento do prato do cardápio com sua respectiva receita, isto é, ingrediente e quantidade. Vale lembrar que já existem classes implementadas para os pratos (`Dish`) e os ingredientes (`Ingredient`). Além disso, a classe que você vai implementar precisa conter um atributo `dishes`, que deverá ser um _set_ que liste todos os pratos presentes no arquivo csv.

### Implementação

Implemente a classe `MenuData` no arquivo `src/services/menu_data.py`.  
O teste utiliza o [arquivo de mock `tests/mocks/menu_base_data.csv`](./tests/mocks/menu_base_data.csv).

Ao longo da sua implementação você deve garantir que:

- a classe, ao ser instanciada, recebe o caminho para o arquivo csv no parâmetro `source_path`;

- a classe fará a leitura do arquivo csv e baseado em seu conteúdo fará as devidas instanciações de pratos e ingredientes;

- a classe contenha o atributo `dishes` que deverá ser um _set_ com todos os pratos devidamente instanciados;

- cada um dos pratos contenha sua respectiva receita, isto é, seus ingredientes e quantidades, bem como seu preço.

## 4 - Geração dos cardápios

Atualmente o cardápio do Restaurante 🍝 🦐 Chapa Quente 🍛 🥘 tem estrutura fixa e, apesar disso não ser um problema, as pessoas fundadoras do estabelecimento desejavam que este cardápio fosse dinâmico, isso porque muitas das pessoas que frequentam o restaurante possuem restrições alimentares, e seria ideal mostrar-lhes o cardápio contendo apenas os pratos que possam comer.

Com este objetivo, a equipe que trabalhou no projeto antes de você começou a implementação de uma classe que interagisse ao mesmo tempo com o cardápio e com o estoque, e que ainda pudesse exibir os pratos do cardápio de acordo com uma determinada restrição alimentar. Sua tarefa neste requisito é fazer a implementação do método que mostrará os cardápios evitando os pratos com determinada restrição alimentar.

### Implementação

Implementar o método `get_main_menu` dentro da classe `MenuBuilder` que se encontra no arquivo `src/services/menu_builder.py`. O método tem como parâmetro opcional uma restrição que deve ser levada em conta na hora de gerar o cardápio.

Seguindo a assinatura do método que foi deixada pela equipe anterior, o retorno deste método deve ser do tipo `List[Dict]`. Assim, é necessário que o método retorne uma lista de dicionários que contenham as chaves `dish_name`, `ingredients`, `price` e `restrictions` que se referem, respectivamente, ao **nome** do prato, **ingredientes** que o compõem, seu **preço** no cardápio e **restrições** daquele mesmo prato.

Ao longo de implementação deve-se garantir que:

- a classe possa ser instanciada corretamente;

- o método `get_main_menu` retorna uma lista de dicionários com o cardápio completo quando não é passado nenhum parâmetro;

- o método `get_main_menu` retorna uma lista de dicionários com o cardápio correto respeitando a restrição alimentar passada como parâmetro;

## 5 - Estoque de ingredientes

A gestão de estoque do restaurante também é feita por meio de um arquivo csv. Para o controle de estoque é usado um arquivo em que cada uma das linhas contém um ingrediente e sua respectiva quantidade inicial no estoque. Seu objetivo neste requisito é finalizar o desenvolvimento da classe que fará o controle do estoque de ingredientes.

Assim como no requisito anterior, o time que trabalhou antes já iniciou a implementação da classe e cabe a você finalizar esta implementação. Deve-se implementar dois métodos para a classe: `check_recipe_availability` e `consume_recipe`.

O primeiro dos métodos (`check_recipe_availability`) deve checar se a receita passada como parâmetro está ou não disponível para consumo, para isso, deve retornar `False` caso um ingrediente da receita não exista no estoque ou caso não exista quantidade suficiente destes ingredientes em estoque e `True`  caso o prato esteja disponível para consumo.

O segundo método (`consume_recipe`) também recebe uma receita como parâmetro, mas deve subtrair a quantidade de ingredientes usados na receita do total disponível em estoque. Vale lembrar que a subtração só deve acontecer caso a receita esteja disponível para consumo, caso contrário, deverá ser levantada uma exceção `ValueError`.

### Implementação

A classe `InventoryMapping` se encontra no arquivo `src/services/inventory_control.py`, nela você deverá implementar os métodos `check_recipe_availability` e `consume_recipe`. Ao longo da sua implementação você deve garantir que:

- A classe possa ser devidamente instanciada;

- o método `check_recipe_availability` retorna `True` caso a receita esteja disponível para consumo e `False` caso contrário;

- o método `consume_recipe` subtrai os ingredientes da receita do total disponível em estoque caso a receita esteja disponível para consumo e levanta uma exceção `ValueError` caso contrário.

## 6 - Cardápios baseados no estoque 

Com a implementação que foi feita até o momento, o método gerador de cardápios, `get_main_menu`, considera apenas as restrições alimentares para fazer a geração do cardápio com os pratos que as pessoas podem comer. Isso ainda é um problema, dado que ainda não é feita a verificação se os ingredientes do prato estão disponíveis em estoque.

A tarefa neste requisito é complementar a implementação do método `get_main_menu` para considerar a disponibilidade em estoque dos ingredientes do prato além das restrições alimentares. Assim, o restaurante possuirá a ferramenta capaz de gerar cardápios dinâmicos considerando restrições alimentares e disponibilidade em estoque.

### Implementação

Você deve complementar a implementação do método `get_main_menu`, feito no requisito 4. O método agora precisa considerar também a disponibilidade em estoque dos ingredientes dos pratos. Use a classe implementada no requisito anterior, `InventoryMapping`, para ter acesso a informações do estoque.

Ao longo de sua implementação você deve garantir que:

- o método `get_main_menu` retorna uma lista de dicionários com o cardápio completo caso não exista restrição e todos os ingredientes estiverem disponíveis;

- o método `get_main_menu` retorna uma lista de dicionários com os cardápios corretos respeitando a restrição alimentar passada como parâmetro e também a disponibilidade de ingredientes no estoque;
