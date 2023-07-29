# elementary-cellular-automaton-2018
An old script to generate, visualize and play with elementary cellular automata


# What is this?
This repository stores my first bigger Python project I had worked on (off GitHub):
The monolithic [*elementary cellular automaton* script](./ECAutomaton.py) (to be solely interacted with directly in console) boasts over 1000 lines of completely unreadable spaghetti code from when I was learning Python.

I apparently even wrote a ['user manual'](./ECA_User_Manual.pdf) for it *(not very useful since didn't know any $\LaTeX$ at the time.)*


# How could I use it?
Run `ECAutomaton.py` and use input/output to navigate console menus.

*(Note to self: use `cmd` to display all 'commands' even not listed in the 'help' menu.)*


# What can it do?

Customize and generate visualizations in console and PNG.

<details><summary>List of practical functionality</summary>

- `info` Information about the script itself!
- `links` External resources on the topic!
- `examples` Built-in examples.
- `image` Save & show last pattern as image.
- `print` / `print small` / `print small2` Print pattern to console.
- `preset cells` For how Unicode art is printed.

- `randrule` / `rr` Randomize rule and print result.
- `randseed` / `rs` Randomize seed and print result.
- `randseed+` / `rs+` *Advancedly* randomize seed and print result.

- `rule` Change generation rule/behaviour.
- `seed` Change seed generation.
- `edges` Change behaviour at cell boundaries (wrap or fixed).
- `history` Change imaginary -1st generation (copy of 0th, fixed or custom.
- `iterations` How many rows are generated.
- `merge` Comparing two different generated patterns.
- `order` Toggles the *order* (first, second).
- `shift` linear Shift of iterations for display purposes.
- `rule110` Enter 'gliders' (Cook notation).
- `rule110 ether` Toggle display of gliders against 'background.'
- `funfact` 12 fun facts.

<details>


# Gallery

## Screenshot

![screenshot](./ECA_screenshot.png)

## Built-in examples.

![example01](Gallery/examples_upscaled/ex1_Rule-60_(0SLz-76).png)

![example02](Gallery/examples_upscaled/ex2_Rule-90_(0SLz-79).png)

![example03](Gallery/examples_upscaled/ex3_Rule-184_(0SLz-82).png)

![example04](Gallery/examples_upscaled/ex4_Rule-150_(0SLz-84).png)

![example05](Gallery/examples_upscaled/ex5_Rule-30_(0SLz-86).png)

![example06](Gallery/examples_upscaled/ex6_Rule-106_(0SLz-88).png)

![example07](Gallery/examples_upscaled/ex7_Rule-110_(0SLz-90).png)

![example08](Gallery/examples_upscaled/ex8_Rule-214R_(0SLz-92).png)

![example09](Gallery/examples_upscaled/ex9_Rule-73R_(0SLz-94).png)

![example10](Gallery/examples_upscaled/ex10_Rule-150R_(0SLz-96).png)

![example11](Gallery/examples_upscaled/ex11_Rule-105R_(0SLz-98).png)

![example12](Gallery/examples_upscaled/ex12_Rule-60R_(0SLz-103).png)

![example13](Gallery/examples_upscaled/ex13_Rule-146R_(0SLz-105).png)

![example14](Gallery/examples_upscaled/ex14_Rule-210R_(0SLz-107).png)

![example15](Gallery/examples_upscaled/ex15_Rule-202R_(0SLz-109).png)

![example16](Gallery/examples_upscaled/ex16_Rule-218R_(0SLz-111).png)

![example17](Gallery/examples_upscaled/ex17_Rule-90R_(0SLz-114).png)

## More examples

### Big

<details><summary>1080 generations of rule 30.</summary>

![rule30](Gallery/Rule30_bnw7p-6.png)

</details>

<details><summary>1024 generations of rule 150 order 2.</summary>

![rule150](Gallery/Rule-150R_8QlL-5.png)

</details>

<details><summary>2048 generations of rule 150 order 2.</summary>

![rule78](Gallery/Rule-78R_lvTB-5.png)

</details>

<details><summary>2525 generations of rule 218 order 2.</summary>

![rule78](Gallery/Rule-218R_Lnat-10_HS.png)

</details>

<details><summary>4096 generations of rule 226 order 2.</summary>

![rule78](Gallery/Rule-226R_bYHc-65.png)

</details>

### Colored

<details><summary>1000 generations of rule 110, with/without ether highlight.</summary>

<div style="position:relative">

<img align="left" src="/Gallery/colored/Rule110_lfl9h-4.png" width=384 alt="xdivision animation">

<img align="center" src="/Gallery/colored/Rule110_lfl9h-8-ether.png" width=384 alt="xdivision endresult">

</div>

</details>

<details><summary>512 generations of rule 90 order 2, flood-fill color.</summary>

<div style="position:relative">

<img align="left" src="/Gallery/Gallery/colored/Rule-90R_(-lDo-9)_resized.png" width=384 alt="xdivision animation">

<img align="center" src="/Gallery/colored/Rule-90R_(-lDo-9)_coloured_resized.png" width=384 alt="xdivision endresult">

</div>

</details>

