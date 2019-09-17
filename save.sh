#!/bin/bash



echo $1 >> savefile
$1 |& tee -a savefile



