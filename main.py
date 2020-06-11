from vm import Vm

if __name__ == '__main__':
    program = '''n1029 = pair
n1033 = ` ` S ` ` B B ` ` C isEmptyList emptyList ` ` C B ` ` S ` ` B C ` ` B ` B B ` B n1029 ` C n1033
n1034 = ` ` S ` ` B B ` ` B B ` ` C isEmptyList emptyList ` ` C ` ` B B B ` ` S ` ` B S ` ` B ` B C ` ` B ` B ` B B ` ` B ` B ` B n1029 C ` ` C ` ` B B ` ` B C ` C n1034 ` ` C + 1
n1035 = ` ` S ` ` C isEmptyList 0 ` ` B ` + 1 ` ` B n1035 tail
n1036 = ` ` S ` ` B S isEmptyList ` ` C B ` ` B ` C ` ` B B n1029 ` C n1036
n1037 = ` ` S ` ` B S ` ` B ` B B isEmptyList ` ` C ` ` B B B ` ` C ` ` B S ` ` B ` B C ` ` B ` B ` B C ` ` B ` B ` B ` C n1037 ` ` C ` ` B C ` ` B ` B B ` C I I I
n1038 = ` ` S ` ` B S ` ` B ` B B isEmptyList ` ` C ` ` B B B ` ` C ` ` B C ` ` B ` B B ` ` B ` B C ` ` B ` S B ` ` B C ` C n1038 I
n1039 = ` ` C ` ` C n1038 emptyList ` C n1036
n1040 = ` ` C ` ` B B ` ` C n1038 emptyList ` ` C ` ` B S ` ` B ` B C ` ` C ` ` B B S ` C n1029 I
n1041 = ` ` S ` ` C ` ` C <= 0 emptyList ` ` S ` ` B n1029 ` ` C - 1 ` ` B n1041 ` ` C - 1
n1042 = ` ` S ` ` B n1033 n1041 ` ` C ` ` B C ` ` B ` B - - 1
n1043 = ` ` C B ` ` S ` ` B C ` ` B ` B B ` ` C == 0 ` ` B ` C n1043 ` ` C - 1
n1044 = ` ` C ` ` C n1037 0 +
n1045 = ` ` C ` ` B B B ` ` S ` ` B S ` ` B ` B B ` ` B ` B S ` ` C ` ` B B ` ` B B ` ` C == 0 n1029 ` ` B ` B ` C ` ` B B n1029 ` ` B C ` ` B ` C n1045 ` ` C - 1
n1048 = ` ` C B ` ` B ` C ` ` B C ` C n1037 ` ` C ` ` B S ` ` B ` B C ` ` C ` ` B C ` ` B ` B S ` ` C ` ` B C ` B B I I I
n1053 = ` ` S ` ` B B ` ` C isEmptyList emptyList ` ` S B ` ` C ` ` B S ` ` B ` B S ` ` B ` B ` B S ` ` C ` ` B S ` ` B ` B S ` ` B ` B ` B B ` ` B ` B ` B C ` ` B ` B ` B ` C ` ` B C ` ` B C ` ` B ` B n1036 n1036 ` ` C ` ` B B ` ` B B n1040 ` ` B ` B ` B C ` ` S ` ` B S ` ` B ` B S ` ` B ` B ` B ` ` S I I ` ` C ` ` B C ` B B I C ` ` S ` ` B C ` ` B ` B C ` ` B ` B ` B n1053 ` ` B ` B ` C n1040 ` ` C ` ` B C ` B B I I ` ` S ` ` B C ` ` B ` B C ` ` B ` B ` B n1053 ` ` B ` B ` C n1040 C I
n1054 = ` ` S ` ` B B ` ` S isEmptyList I ` ` S B ` ` C ` ` B B ` ` B B ` ` B S ` C isEmptyList ` ` B ` B ` S I ` ` B ` B ` B ` B K ` ` S ` ` B C ` ` B ` B S ` ` B ` B ` B C ` ` S ` ` B S ` ` B ` B B ` ` B ` B C ` ` C ` ` B C ` B B I ` ` B ` C ` ` B B pair ` C n1054 ` C n1054
n1056 = ` ` C ` ` B n1054 ` ` C n1053 < <
n1060 = pair
n1064 = ` ` C ` ` B C ` ` B ` B B ` ` B ` B B ` ` B ` B pair n1060 n1060
n1067 = ` ` C B ` ` C ` ` B B B ` ` C ` ` B B ` ` B C ` ` B ` B B ` ` B ` B n1060 + +
n1068 = ` ` C ` ` B B n1033 ` C n1067
n1069 = ` ` B ` pair 0 ` ` C pair ` ` pair emptyList emptyList
n1070 = ` ` B ` B ` pair 0 ` ` C ` ` B B pair ` ` C pair emptyList
n1073 = ` ` B ` B ` C ` ` B n1033 n1041 ` ` B C ` ` B ` B n1060 +
n1074 = ` ` B ` B ` C ` ` B n1033 n1041 ` ` C ` ` B B ` ` B B n1060 +
n1075 = ` ` S ` ` B S ` ` B ` B S ` ` B ` B ` B S ` ` B ` B ` B ` B n1036 ` ` S ` ` B S ` ` B ` B C ` ` B ` B ` B S ` ` B ` B ` B ` B n1036 ` ` S ` ` B S ` ` B ` B S ` ` B ` B ` B B ` ` B ` B ` B n1036 ` ` C ` ` B C ` ` B ` B B n1073 I ` ` C ` ` B C ` ` B ` B B ` ` B ` B C ` ` C ` ` B B ` ` B B n1073 ` ` C ` ` B C ` ` B ` B - + 1 I ` ` C ` ` B C ` ` B ` B B n1074 I ` ` C ` ` B C ` ` B ` B C ` ` B ` B ` B B ` ` B C ` ` B ` B n1074 ` ` C ` ` B C ` ` B ` B - + 1 ` ` C - 1
n1076 = ` ` B ` B ` B ` B n1039 ` ` B ` B ` B ` C ` ` B n1033 n1041 ` ` C ` ` B C ` ` B ` B B ` ` B ` B C ` ` C ` ` B B ` ` B B n1073 + I
n1077 = ` ` S ` ` B C ` ` B ` B B ` ` B ` B ` ` S C I >= <
n1078 = ` ` C B ` ` C ` ` B B B ` ` B ` B ` C B ` ` B ` B ` C ` ` B B B ` ` C ` ` B B ` ` B C ` ` B ` B B ` ` B ` B C ` ` B ` B ` B B ` ` B ` B ` B ` ` S C I ` ` C ` ` B S ` ` B ` B B n1077 + ` ` C ` ` B S ` ` B ` B B n1077 +
n1079 = ` ` S ` ` B n1036 ` ` C ` ` B n1033 n1041 ` ` C ` ` B n1060 ` + 1 0 ` ` C ` ` B n1033 n1041 ` ` B ` n1060 0 ` + 1
n1080 = ` ` B ` B tail ` ` C ` ` B S ` ` C ` ` B B n1037 ` ` B ` pair 0 n1079 ` ` B ` C B ` ` C ` ` B C ` ` B ` B B ` ` B ` B C ` ` C ` ` B C ` ` B ` B B ` ` B ` B C ` ` B ` B ` S ` ` B B ` ` B pair ` ` C + 1 ` ` B ` C ` ` B B ` ` B S ` ` C == 0 ` ` C ` ` B C ` ` B ` B B ` ` B ` B n1029 ` ` S ` ` B S ` ` B ` B n1060 ` ` B ` B ` + 1 ` C % ` ` B ` B ` + 1 ` C / I I I
n1081 = ` ` S ` ` C ` ` C == 0 emptyList ` ` S ` ` B n1029 ` ` C % 2 ` ` B n1081 ` ` C / 2
n1082 = ` ` S ` ` C ` ` C == 0 ` ` pair 0 emptyList n1081
n1083 = ` ` S ` ` C ` ` C <= 0 0 ` ` B head ` ` S ` ` B n1040 ` ` B n1042 ` ` C + 1 ` C ` ` B >= ` ` S * I
n1084 = ` ` C ` ` B S ` ` C ` ` B C ` ` B ` B B ` ` C ` ` B C ` ` B ` B S ` ` C ` ` B B ` ` B C ` ` B ` B S ` ` C ` ` B B ` ` B B ` ` B B ` ` C ` ` B S ` ` C B ` n1029 ` ` n1060 0 0 I ` ` C ` ` B C ` ` B ` B B ` ` B ` B n1036 n1080 I ` ` C ` ` B C ` ` C ` ` B B ` ` C < 0 ` ` C ` ` B pair ` ` C ` ` B n1060 ` ` C + 1 0 emptyList emptyList ` ` B n1083 n1035 n1082 ` ` S ` ` S ` ` C >= 0 I negate
n1085 = ` n1084 ` S K
n1089 = ` ` B n1039 ` ` C ` ` C n1034 ` ` C ` ` B B ` ` B n1033 n1090 ` C n1060 0
n1090 = ` ` B n1039 ` ` C ` ` C n1034 ` ` C ` ` B C ` ` B ` B n1033 ` ` C ` ` B C ` ` B ` B n1040 ` ` C ` ` B C ` ` C ` ` B B ` ` B n1034 n1081 ` ` B ` C ` ` B B pair ` ` B ` C + ` ` C * 31 0 ` ` C ` ` B == head 1 tail 0
n1122 = ` ` S ` ` B S ` ` C ` ` B B isEmptyList ` n1122 ` ` pair 0 emptyList ` ` B ` C ` ` C B ` ` B ` B ` B ` ` S ` ` C ` ` C >= 8 ` ` n1070 ` ` pair n1138 ` ` pair emptyList ` ` pair emptyList emptyList emptyList ` ` S ` ` B n1070 ` ` B ` pair n1137 ` ` C ` ` B pair ` ` C pair emptyList ` ` pair emptyList emptyList n1123 ` ` S ` ` B C ` ` B ` B C ` ` B ` C ` ` B C ` ` C ` ` B C ` ` B ` B n1078 n1060 ` ` ` ` n1064 0 0 6 6 ` ` C + 1 I ` ` B I head
n1123 = ` ` B ` pair ` ` pair ` ` pair 0 0 ` ` pair ` ` pair 1 0 ` ` pair ` ` pair 4 0 ` ` pair ` ` pair 2 1 ` ` pair ` ` pair 4 1 ` ` pair ` ` pair 1 2 ` ` pair ` ` pair 2 2 ` ` pair ` ` pair 3 2 ` ` pair ` ` pair 0 3 ` ` pair ` ` pair 2 3 ` ` pair ` ` pair 0 4 ` ` pair ` ` pair 3 4 ` ` pair ` ` pair 4 4 emptyList ` ` S ` ` B pair ` ` C ` ` B n1068 n1085 ` ` n1060 ` negate 5 ` negate 5 ` ` C ` ` B pair n1124 emptyList
n1124 = ` ` S ` ` C ` ` C < 4 emptyList ` ` C ` ` C ` ` C == 4 ` ` n1036 ` ` ` ` n1075 ` negate 1 ` negate 1 7 7 ` ` ` ` n1075 ` negate 6 ` negate 6 5 5 ` ` n1036 ` ` ` ` n1076 ` negate 1 ` negate 1 7 7 ` ` ` ` n1076 ` negate 6 ` negate 6 5 5
n1137 = 0
n1138 = 1
n1139 = ` ` pair n1122 ` ` pair n1181 emptyList
n1140 = ` ` B ` C ` C n1141 ` ` S ` ` C isEmptyList ` ` pair 0 ` ` pair ` ` pair ` negate 1 emptyList ` ` pair emptyList emptyList I
n1141 = ` ` S ` ` B C ` ` C ` ` B C ` ` B ` B S ` ` S ` ` B S ` ` B ` B C ` ` B ` B ` B B ` ` C ` ` B C ` ` B ` B C ` ` B ` B ` B S ` ` B ` C ` ` B C ` ` B ` B C ` ` B ` B ` B S ` ` C ` ` B C ` ` B ` B B ` ` B ` B S ` ` B ` B ` B S ` ` B ` C ` ` B S ` ` B ` B B ` ` B ` B C ` C ` ` B == ` ` C n1043 0 ` ` C ` ` B B ` ` B B ` C n1141 ` ` C ` ` B B ` ` B pair ` ` C n1043 0 ` ` B ` pair emptyList ` ` C pair emptyList ` ` C ` ` B B ` ` B B ` ` S ` ` B B ` ` B pair ` ` C n1043 0 ` ` B ` C pair ` ` C ` ` B pair ` ` C n1043 2 emptyList ` ` S ` ` B B ` ` B pair ` ` C n1043 0 ` ` C ` ` B B ` ` B pair ` ` C n1043 1 ` ` C pair emptyList ` ` B ` B n1056 ` ` C ` ` B B ` ` B n1036 ` ` C n1043 2 ` ` C n1043 2 ` ` C n1043 1 ` ` B C ` ` B ` C I ` ` C n1043 1 ` n1043 n1139 ` ` C n1043 0
n1160 = ` ` pair 0 ` ` pair 0 ` ` pair 0 ` ` pair 0 ` ` pair 0 ` ` pair 0 ` ` pair 0 ` ` pair 0 ` ` pair 0 emptyList
n1161 = ` ` pair ` ` pair 87040 emptyList ` ` pair ` ` pair 1315844 emptyList ` ` pair ` ` pair 4474034 emptyList ` ` pair ` ` pair 5592356 emptyList ` ` pair ` ` pair 0 emptyList ` ` pair ` ` pair 1792 emptyList ` ` pair ` ` pair 6912 emptyList ` ` pair ` ` pair 6912 emptyList ` ` pair ` ` pair 10496 emptyList ` ` pair ` ` pair 16128 emptyList ` ` pair ` ` pair 0 emptyList ` ` pair ` ` pair 6407704 emptyList ` ` pair ` ` pair 4194704 emptyList ` ` pair ` ` pair 6866458 emptyList ` ` pair ` ` pair 8255455 emptyList ` ` pair ` ` pair 0 emptyList ` ` pair ` ` pair 524290 emptyList ` ` pair ` ` pair 0 emptyList ` ` pair ` ` pair 262145 emptyList ` ` pair ` ` pair 8126495 emptyList ` ` pair ` ` pair 0 emptyList ` ` pair ` ` pair 6391704 emptyList ` ` pair ` ` pair 4210704 emptyList ` ` pair ` ` pair 6841242 emptyList ` ` pair ` ` pair 8255455 emptyList ` ` pair ` ` pair 0 emptyList ` ` pair ` ` pair 530434 emptyList ` ` pair ` ` pair 6144 emptyList ` ` pair ` ` pair 268289 emptyList ` ` pair ` ` pair 8132639 emptyList ` ` pair ` ` pair 6144 emptyList ` ` pair ` ` pair 1050648 emptyList ` ` pair ` ` pair 530528 emptyList ` ` pair ` ` pair 399744 emptyList ` ` pair ` ` pair 100448 emptyList ` ` pair ` ` pair 6168 emptyList ` ` pair ` ` pair 100358 emptyList ` ` pair ` ` pair 399384 emptyList ` ` pair ` ` pair 530528 emptyList ` ` pair ` ` pair 1055104 emptyList ` ` pair ` ` pair 2103392 emptyList ` ` pair ` ` pair 2103320 emptyList ` ` pair ` ` pair 1050630 emptyList ` ` pair ` ` pair 528408 emptyList ` ` pair ` ` pair 2490464 emptyList ` ` pair ` ` pair 2177408 emptyList ` ` pair ` ` pair 2128896 emptyList ` ` pair ` ` pair 2118656 emptyList ` ` pair ` ` pair 14427 emptyList ` ` pair ` ` pair 4460591 emptyList ` ` pair ` ` pair 14389 emptyList ` ` pair ` ` pair 2118714 emptyList ` ` pair ` ` pair 2101307 emptyList ` ` pair ` ` pair 2107442 emptyList ` ` pair ` ` pair 512 emptyList ` ` pair ` ` pair 3167488 emptyList ` ` pair ` ` pair 3474005 emptyList ` ` pair ` ` pair 80 emptyList ` ` pair ` ` pair 0 emptyList ` ` pair ` ` pair 589896 emptyList ` ` pair ` ` pair 393264 emptyList ` ` pair ` ` pair 2506290 emptyList ` ` pair ` ` pair 1655116 emptyList ` ` pair ` ` pair 1605836 emptyList ` ` pair ` ` pair 2574706 emptyList ` ` pair ` ` pair 152864 emptyList ` ` pair ` ` pair 2443632 emptyList ` ` pair ` ` pair 1605836 emptyList ` ` pair ` ` pair 1589580 emptyList ` ` pair ` ` pair 2506290 emptyList ` ` pair ` ` pair 393224 emptyList ` ` pair ` ` pair 553985 emptyList ` ` pair ` ` pair 4242560 emptyList emptyList
n1162 = ` C ` C ` ` C ` ` B C ` ` S ` ` B S ` ` C ` ` B S ` ` B ` B ` ` S C I ` ` C ` ` B B ` ` B ` ` S C I ` ` S ` ` B ` ` S C I ` ` C >= 0 ` ` C <= 2 ` ` C >= 0 ` ` C <= 2 ` ` C ` ` B B + ` * 3 ` negate 1
n1163 = ` ` S ` ` C isEmptyList 0 ` ` C I ` ` C ` ` B B + ` ` B ` * 7 n1163
n1164 = ` ` S ` ` B S ` ` B ` B S ` ` B ` B ` B S ` ` B ` B ` B ` B ` ` S C I ` ` S ` ` B S ` ` B ` B B ` ` B ` B S ` ` B ` B ` B ` ` S C I ` ` C ` ` B C ` ` B ` B B ` ` B ` B == n1043 I ` ` C ` ` B C ` ` B ` B C ` ` B ` B ` B B ` ` B ` B ` B == ` ` C ` ` B B ` ` B B n1043 + I ` ` C ` ` B C ` ` B ` B C ` ` B ` B ` B B ` ` B ` B ` B == ` ` C ` ` B B ` ` B B n1043 ` ` C ` ` B S ` ` B ` B + + I I
n1165 = ` ` S ` ` B S ` ` B ` B ` ` S I I ` ` S ` ` B S ` ` B ` B ` ` S I I ` ` S ` ` B S ` ` B ` B ` ` S I I n1166 n1167 ` ` C ` ` C n1164 0 4 ` ` C ` ` C n1164 2 2
n1166 = ` ` S ` ` B S ` ` B ` B ` ` S I I ` ` S ` ` B S ` ` B ` B ` ` S I I ` ` C ` ` C n1164 0 1 ` ` C ` ` C n1164 3 1 ` ` C ` ` C n1164 6 1
n1167 = ` ` S ` ` B S ` ` B ` B ` ` S I I ` ` S ` ` B S ` ` B ` B ` ` S I I ` ` C ` ` C n1164 0 3 ` ` C ` ` C n1164 1 3 ` ` C ` ` C n1164 2 3
n1168 = ` ` S ` ` B ` ` S I I ` ` S ` ` B ` ` S I I ` ` C n1165 1 ` ` C n1165 2 ` ` C ` ` B == ` ` B n1035 ` ` C n1040 ` ` B C ` ` C == 0 9
n1169 = ` ` C ` ` B B ` ` B ` B n1044 ` ` C ` ` B C n1034 0 ` ` C ` ` B C ` ` B ` B B ` ` C ` ` B C ` ` B ` B C ` C == 0 ` ` S ` ` C ` ` C == 4 2 ` ` B ` - 1 ` ` C % 2
n1170 = ` ` S ` ` B B ` ` B B ` ` C ` ` B C ` ` B ` B n1048 ` ` B n1033 n1172 ` ` C ` ` B B ` ` B < head head ` ` B ` S ` ` B C ` ` B ` B S ` ` S ` ` B B ` ` B S ` ` B ` B S ` ` C ` ` B B ` ` B C ` C n1165 ` pair 10 ` ` B ` B ` S ` ` B S ` ` B ` C n1171 ` pair 0 ` ` S ` ` B S ` ` B ` B S ` ` B ` B ` B S ` ` B ` C ` ` B B ` ` B B ` ` C == 0 ` ` B C ` ` B ` B pair ` ` S ` ` B S ` ` B ` B - ` C n1169 ` ` B ` C n1169 ` - 3 ` ` C ` ` B C ` ` B ` B B ` ` B ` B C ` ` B ` B ` B pair ` ` B ` B ` B negate ` ` B ` B ` B head ` ` C ` ` B B ` ` B C ` ` B ` C n1170 ` - 3 ` ` C - 1 I ` ` B C n1045
n1171 = ` ` B isEmptyList ` ` C n1040 ` ` C == 0
n1172 = ` ` C ` ` B n1033 ` ` C ` ` B n1040 ` ` C ` ` C n1034 pair 0 ` ` C ` ` B == head 0 ` ` B I tail
n1173 = ` ` B ` B I ` ` B ` B tail ` ` C ` ` B C n1170 3
n1174 = ` ` S ` ` B B ` ` B B ` ` C ` ` C < 0 n1160 ` ` S ` ` B S ` ` B ` B B ` ` C ` ` B S ` ` B ` S ` ` B ` ` S I I n1168 ` ` B ` B C ` ` C ` ` B C ` ` B ` B == ` C n1043 0 I ` ` B ` B ` S ` ` S ` ` B S ` ` C ` ` B S ` ` C ` ` B S ` ` B ` B ` ` S I I ` C n1165 ` ` B isEmptyList ` ` C n1040 ` ` C == 0 I ` ` S ` ` B C ` ` B ` S n1045 ` ` B ` C n1173 ` - 3 ` - 3 ` ` C ` ` B C ` ` B ` B B ` C n1045 I
n1175 = ` ` S ` ` B n1060 ` ` C % 3 ` ` C / 3
n1176 = ` ` C ` ` B B ` ` C ` ` B C ` ` C ` ` B B ` ` C == 1 ` ` C pair emptyList emptyList n1175
n1177 = ` ` C ` ` B B ` ` C ` ` B B ` ` C ` ` C == 2 emptyList ` ` C pair emptyList n1175
n1178 = ` ` S ` ` B B ` ` C isEmptyList ` n1069 ` ` pair n1160 ` ` pair emptyList emptyList ` ` S ` ` B C ` ` B ` C ` ` B C ` ` B ` S ` ` B S ` ` C ` ` B B n1168 ` ` B n1069 ` ` B ` pair n1160 ` ` C pair emptyList ` ` C ` ` B B B ` ` C ` ` B C ` ` B ` B B ` ` B ` B B ` ` B ` C ` ` B B ` ` B ` S ` ` B ` B n1069 ` ` C ` ` B B pair ` ` C pair emptyList ` ` S ` ` B C ` ` B ` S n1171 ` ` B ` B n1056 ` C ` ` B n1029 n1163 I ` ` C ` ` B C ` C n1174 1 n1162 ` ` C n1043 1 ` ` C n1043 0
n1179 = ` ` S ` ` C isEmptyList ` n1179 ` ` pair n1160 ` ` pair emptyList emptyList ` ` S ` ` B ` C ` ` C ` ` B B ` ` B ` S ` ` C ` ` C == 0 ` ` pair ` n1089 n1161 emptyList ` ` S ` ` B C ` ` B ` C ` ` B C ` ` B ` C ` ` B B pair ` ` B ` C pair ` ` C ` ` B pair ` ` C ` ` B n1068 n1085 ` ` n1060 0 ` negate 6 emptyList ` ` B n1039 ` ` C ` ` C n1034 n1177 0 ` ` B n1039 ` ` C ` ` C n1034 n1176 0 ` ` B ` - 5 n1035 ` ` C n1043 1 ` ` C n1043 0
n1180 = ` ` B ` B ` ` S n1070 n1179 ` ` C ` ` B C ` ` B ` B n1043 n1178 1
n1181 = ` ` B ` B ` ` S ` ` B n1070 ` ` B ` pair n1138 ` ` C ` ` B pair ` ` B I ` ` C n1043 1 ` ` pair emptyList emptyList ` ` C n1043 2 n1180
operationSystem = n1140'''

    vm = Vm()
    for line in program.split('\n'):
        vm.execute_statement(line)

    print(vm.eval(vm.parse_exp('` ` operationSystem emptyList ` ` pair 0 0')))