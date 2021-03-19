---
title: "Knuckle Tattoo: A Recursive Word Search Puzzle"
date: 2021-03-19
category: "puzzles"
draft: false
tags: ["open data", "fun", "python", "word puzzle"]
slug: "knuckle-tattoo"
---

Introducing **𝕜𝕟𝕦𝕔𝕜𝕝𝕖 𝕥𝕒𝕥𝕥𝕠𝕠** -- a recursive word search puzzle. This puzzle was created by brothers Philip and Stephen Shemella.


![self made knuckle tattoo](/images/fist/selfmade.jpg)

<sup>_source: [Edward Bishop](https://www.creativeboom.com/inspiration/knuckles-photographer-documents-the-fascinating-world-of-knuckle-tattoos-/)_</sup>


## the puzzle

To solve the puzzle, you are given eight (8) letters. You need to find two commonly-used English words, each with four (4) letters, that could be tattooed across your knuckles. When you fingers are intertwined, the resulting spelling creates two new, commonly-used four letter words. There are often many possibile pairs of words, but only one solution where both the knuckles and the intertwined fingers will result in two sets of valid four-letter words.

Think of this puzzle like New York Times' [Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee), except recursive, and harder on your brain. I suggest using scratch paper.

There are not so many possible puzzles with commonly-used words. That's why I can't give a real, working example.

_But here's a hypothetical puzzle_: You are provided the letters
```txt
A B C D W X Y Z
```
If you tattooed `ABCD` on one hand, and `WXYZ` on the other hand, then one variation of intertwined the fingers would spell `AWBX` and `CYDZ`. If this were a real example, all four words would be valid.

### rules of play

+ All words are easily recognizeable and commonly-used English words. Each puzzle has been hand-selected.

+ All letters provided in alphabetical order, with many puzzles including letters used more than once.

Hints:
    Solving subsequent puzzles should be exponentially faster.

## the first puzzle

Happy solving!

```txt
A E E K N O P S
```

## more puzzles

Solving more puzzles should get exponentially faster.

```txt
A B D D E E I T
```

```txt
B E E E F R T U
```

```txt
A E E I L L R S
```

```txt
A D E F H I L T
```

```txt
E E L N O O P S
```

```txt
A E L N O S S T
```

## even more puzzles

You may see some similar patterns to the other puzzles.

```txt
D E E E N R T U
```

```txt
D E E F I L S T
```

```txt
A E E I L L M S
```

```txt
A D H K L O O Y
```

```txt
E E G I K N N S
```

```txt
A E E I L L S S
```

```txt
D E I I K N S T
```

## other interesting puzzles

An interesting outlier, same rules

```txt
D D D G O O O S
```

An eight-letter final word (should be easier to solve)

```txt
A I N O R S T U
```

_Thanks for playing!_

---
---

### strategies for solving

I won't give any hints or suggest a solving strategy until a later blog post. I'm guessing that people may have wildly divergent ways of solving.

If you are an early solver, please share your solving strategy. I'd like to write a follow-up post that shows different solving methods.

### the background

When tattooing two words across your hands, there are two main variations:

**words across two fists**

![stay true knuckle tattoo](/images/fist/staytrue.png)

<sup>_source: [tattooicon](https://tattooicon.com/blogs/news/best-stay-true-knuckle-tattoos)_</sup>

**words which are legible only when the fingers are intertwined**

![let's fuck knuckle tattoo](/images/fist/letsfuck.jpg)

<sup>_source: [inked](https://www.inkedmag.com/culture/knuckle-tattoos-will-crack#gid=ci0234ff9450032718&pid=olympus-digital-camera)_</sup>

#### What if there was a way to combine these variations, so that each fist spelled a word, **and** when you intertwine your fingers, the tattoos spelled other valid words?!

Being a word geek, I had to know. Now I know.

### puzzle generation source code

For generating the puzzles, please follow the steps in this repository: https://github.com/philshem/knuckle-tattoo