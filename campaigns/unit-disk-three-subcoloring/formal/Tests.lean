import Challenge
open UnitDiskThreeSubcoloring
example : targetWitness [(0,0),(1,0),(2,0)] [0,0,0] = false := by native_decide
example : targetWitness [(0,0),(1,0),(2,0)] [0,1,0] = true := by native_decide
