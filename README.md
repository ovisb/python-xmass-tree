## Project
This is the *Xmas Tree (Python)* project that is part of Hyperskill platform from Jetbrains Academy.

## Project description
Console application for generating one or many christmas trees and adding them to a postcard grid 

How to use:
- You can either input two values or multiple of 4s.

For example:
- An input of `7 2` will generate a tree of `height 7` with a decoration `interval value of 2`, and print it to sdout

```bash
> 7 2
      X
      ^
     /*\
    /*O*\
   /***O*\
  /***O***\
 /*O***O***\
/*O***O***O*\
     | |
```
- An input of `7 2 5 15` will generate the above tree while also trying to insert it into `row 5` and column `15`

```bash
> 7 2 5 15
-------------------------------------------------
|                                                |
|                                                |
|                                                |
|                                                |
|              X                                 |
|              ^                                 |
|             /*\                                |
|            /*O*\                               |
|           /***O*\                              |
|          /***O***\                             |
|         /*O***O***\                            |
|        /*O***O***O*\                           |
|             | |                                |
|                                                |
|                                                |
|                                                |
|                                                |
|                                                |
|                                                |
|                                                |
|                                                |
|                                                |
|                                                |
|                                                |
|                                                |
|                                                |
|                   Merry Xmas                   |
|                                                |
--------------------------------------------------
```

- Multiple of 4 inputs can also be passed to generate and add multiple trees to the Postcard grid

```bash
> 7 3 7 37 4 2 10 25 11 1 5 14 10 4 9 30 5 4 16 19
--------------------------------------------------
|                                                |
|                                                |
|                                                |
|                                                |
|             X                                  |
|             ^                                  |
|            /*\                     X           |
|           /*O*\                    ^           |
|          /*O*O*\            X     /*\          |
|         /*O*O*O*\      X    ^    /*O*\         |
|        /*O*O*O*O*\     ^   /*\  /*****\        |
|       /*O*O*O*O*O*\   /*\ /*O*\/*O*****\       |
|      /*O*O*O*O*O*O*\ /*O*/*****\O*****O*\      |
|     /*O*O*O*O*O*O*O*\***/***O***\**O*****\     |
|    /*O*O*O*O*O*O*O*O*\|/*****O***\| |          |
|   /*O*O*O*O*O*O*OXO*O*/*****O*****\            |
|            | |   ^   /***O*******O*\           |
|                 /*\ /*******O*******\          |
|                /*O*\*O*******O*******\         |
|               /*****\      | |                 |
|              /***O***\                         |
|                 | |                            |
|                                                |
|                                                |
|                                                |
|                                                |
|                   Merry Xmas                   |
|                                                |
--------------------------------------------------


Have fun playing around with the trees drawing!

```

#### Project setup

Install everything (main + dev packages except optional groups)

```sh
peotry install
```

Install main packages only

```sh
peotry install --only main

```

If you need pre-commit

```sh
poetry install --with commit
```

If you decided to install pre-commit you can install .pre-commit files in your repo

```sh
peotry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

If the files are git staged, you can trigger pre-commit manually

```sh
poetry run pre-commit run --all-files
poetry run pre-commit run --hook-stage push -v
```

#### Makefile

Added 'Makefile' to make it easy to validate files
Check bellow command on usage

```sh
make help
```
