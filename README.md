# elementary-cellular-automaton

*A script to experiment with and visualize elementary cellular automata (command-line or PNG).*


# What is this?
This repository stores my first bigger Python project I had worked on (2018, not on GitHub):
The monolithic [*elementary cellular automaton* script](./ECAutomaton.py) proudly boasts over 1000 lines of completely unreadable spaghetti code from when I was learning Python.

I even started using Overleaf to write a (not very useful nor comprehensive) ['user manual.'](./ECA_User_Manual.pdf)


# How could I use it?
Run `ECAutomaton.py` and directly use the command-line to navigate scripted menus and draw ASCII (Unicode) art, etc.

*(Note to self: use `cmd` to display all commands (unlike `help`))*


# What can it do?

Customize and generate visualizations in console and PNG.

<details><summary>List of practical 'commands'.</summary>

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

</details>


# Gallery

## Screenshot

![screenshot](./ECA_screenshot.png)

## Examples

### Built-ins

These are also built-into the script.

<details><summary>Show all.</summary>

> Example 1 Sierpinski Fractal (rule 60)
![example01](Gallery/examples_upscaled/ex1_Rule-60_(0SLz-76).png)

> Example 2 Pascal's triangle modulo 2 (rule 90)
![example02](Gallery/examples_upscaled/ex2_Rule-90_(0SLz-79).png)

> Example 3 Particle collision simulation (rule 184)
![example03](Gallery/examples_upscaled/ex3_Rule-184_(0SLz-82).png)

> Example 4 Triangular fractal pattern (rule 150)
![example04](Gallery/examples_upscaled/ex4_Rule-150_(0SLz-84).png)

> Example 5 Chaos even from simple conditions (rule 30)
![example05](Gallery/examples_upscaled/ex5_Rule-30_(0SLz-86).png)

> Example 6 Rule with growth behaviour of sqrt(x) (rule 106)
![example06](Gallery/examples_upscaled/ex6_Rule-106_(0SLz-88).png)

> Example 7 Rule 110 example
![example07](Gallery/examples_upscaled/ex7_Rule-110_(0SLz-90).png)

> Example 8 Example of a 2nd-order, reversible seed (rule 214R)
![example08](Gallery/examples_upscaled/ex8_Rule-214R_(0SLz-92).png)

> Example 9 Interesting looking rule with individual compartments (rule 73R)
![example09](Gallery/examples_upscaled/ex9_Rule-73R_(0SLz-94).png)

> Example 10 Carpet-pattern-rule (rule 150R)
![example10](Gallery/examples_upscaled/ex10_Rule-150R_(0SLz-96).png)

> Example 11 Chaotic rule distantly resembling organic tissue (rule 105R)
![example11](Gallery/examples_upscaled/ex11_Rule-105R_(0SLz-98).png)

> Example 12 Rule that turns out to be example 4 but rotated 90 degrees (rule 60R)
![example12](Gallery/examples_upscaled/ex12_Rule-60R_(0SLz-103).png)

> Example 13 'Inverted'-rule-version of example 9 (rule 146)
![example13](Gallery/examples_upscaled/ex13_Rule-146R_(0SLz-105).png)

> Example 14 An interesting 2nd-order rule (rule 210R)
![example14](Gallery/examples_upscaled/ex14_Rule-210R_(0SLz-107).png)

> Example 15 Another interesting 2nd-order rule (rule 202R)
![example15](Gallery/examples_upscaled/ex15_Rule-202R_(0SLz-109).png)

> Example 16 And another one (rule 218R)
![example16](Gallery/examples_upscaled/ex16_Rule-218R_(0SLz-111).png)

> Example 17 Pattern with horizontal axis of symmetry (rule 90R)
![example17](Gallery/examples_upscaled/ex17_Rule-90R_(0SLz-114).png)

</details>

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

<img align="left" src="/Gallery/colored/Rule110_lfl9h-4.png" width=384 alt="rule 110">

<img align="center" src="/Gallery/colored/Rule110_lfl9h-8-ether.png" width=384 alt="rule 110 colored">

</div>

</details>

<details><summary>512 generations of rule 90 order 2, flood-fill color.</summary>

<div style="position:relative">

<img align="left" src="/Gallery/colored/Rule-90R_(-lDo-9)_resized.png" width=384 alt="rule 90">

<img align="center" src="/Gallery/colored/Rule-90R_(-lDo-9)_coloured_resized.png" width=384 alt="rule 90 colored">

</div>

</details>
