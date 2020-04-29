
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD CALL COMENTARIO DIV DOIS_PONTOS ERRO EXP IDENTIFICADOR INTEIRO JEQ JLT JUMP LOCALS MOD MULT PRINT PRINT_NL PRINT_STR PUSH_ARG PUSH_INT PUSH_VAR RETURN SET_ARG STORE_ARG STORE_VAR STRING SUBprograma : programa etiqueta instrucao programa : etiqueta : IDENTIFICADOR DOIS_PONTOSetiqueta : instrucao :  ADD\n                |   SUB\n                |   MULT\n                |   DIV\n                |   MOD\n                |   EXP\n                |   RETURN\n                |   PRINT\n                |   PRINT_NL\n                |   COMENTARIOinstrucao :  PUSH_INT INTEIRO\n                |   SET_ARG INTEIRO\n                |   JUMP IDENTIFICADOR\n\t            |   JEQ IDENTIFICADOR\n\t            |   JLT IDENTIFICADOR\n\t            |   PRINT_STR STRINGinstrucao : PUSH_VAR INTEIRO INTEIRO\n              |   PUSH_ARG INTEIRO INTEIRO\n              |   STORE_VAR INTEIRO INTEIRO\n              |   STORE_ARG INTEIRO INTEIRO\n              |   CALL INTEIRO IDENTIFICADOR\n              |   LOCALS INTEIRO INTEIRO'
    
_lr_action_items = {'IDENTIFICADOR':([0,1,4,5,6,7,8,9,10,11,12,13,14,17,18,19,28,29,30,31,32,33,38,40,41,42,43,44,45,],[-2,3,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,30,31,32,-15,-16,-17,-18,-19,-20,44,-21,-22,-23,-24,-25,-26,]),'$end':([0,1,4,5,6,7,8,9,10,11,12,13,14,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,0,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'ADD':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,5,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'SUB':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,6,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'MULT':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,7,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'DIV':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,8,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'MOD':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,9,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'EXP':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,10,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'RETURN':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,11,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'PRINT':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,12,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'PRINT_NL':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,13,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'COMENTARIO':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,14,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'PUSH_INT':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,15,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'SET_ARG':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,16,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'JUMP':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,17,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'JEQ':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,18,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'JLT':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,19,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'PRINT_STR':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,20,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'PUSH_VAR':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,21,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'PUSH_ARG':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,22,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'STORE_VAR':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,23,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'STORE_ARG':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,24,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'CALL':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,25,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'LOCALS':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,27,28,29,30,31,32,33,40,41,42,43,44,45,],[-2,-4,26,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-3,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'DOIS_PONTOS':([3,],[27,]),'INTEIRO':([15,16,21,22,23,24,25,26,34,35,36,37,39,],[28,29,34,35,36,37,38,39,40,41,42,43,45,]),'STRING':([20,],[33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'etiqueta':([1,],[2,]),'instrucao':([2,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> programa etiqueta instrucao','programa',3,'p_programa','registos.py',260),
  ('programa -> <empty>','programa',0,'p_prgram_empty','registos.py',266),
  ('etiqueta -> IDENTIFICADOR DOIS_PONTOS','etiqueta',2,'p_etiqueta','registos.py',272),
  ('etiqueta -> <empty>','etiqueta',0,'p_etiqueta_empty','registos.py',279),
  ('instrucao -> ADD','instrucao',1,'p_instrucao','registos.py',284),
  ('instrucao -> SUB','instrucao',1,'p_instrucao','registos.py',285),
  ('instrucao -> MULT','instrucao',1,'p_instrucao','registos.py',286),
  ('instrucao -> DIV','instrucao',1,'p_instrucao','registos.py',287),
  ('instrucao -> MOD','instrucao',1,'p_instrucao','registos.py',288),
  ('instrucao -> EXP','instrucao',1,'p_instrucao','registos.py',289),
  ('instrucao -> RETURN','instrucao',1,'p_instrucao','registos.py',290),
  ('instrucao -> PRINT','instrucao',1,'p_instrucao','registos.py',291),
  ('instrucao -> PRINT_NL','instrucao',1,'p_instrucao','registos.py',292),
  ('instrucao -> COMENTARIO','instrucao',1,'p_instrucao','registos.py',293),
  ('instrucao -> PUSH_INT INTEIRO','instrucao',2,'p_instrucao_arg1','registos.py',300),
  ('instrucao -> SET_ARG INTEIRO','instrucao',2,'p_instrucao_arg1','registos.py',301),
  ('instrucao -> JUMP IDENTIFICADOR','instrucao',2,'p_instrucao_arg1','registos.py',302),
  ('instrucao -> JEQ IDENTIFICADOR','instrucao',2,'p_instrucao_arg1','registos.py',303),
  ('instrucao -> JLT IDENTIFICADOR','instrucao',2,'p_instrucao_arg1','registos.py',304),
  ('instrucao -> PRINT_STR STRING','instrucao',2,'p_instrucao_arg1','registos.py',305),
  ('instrucao -> PUSH_VAR INTEIRO INTEIRO','instrucao',3,'p_instrucao_arg2','registos.py',312),
  ('instrucao -> PUSH_ARG INTEIRO INTEIRO','instrucao',3,'p_instrucao_arg2','registos.py',313),
  ('instrucao -> STORE_VAR INTEIRO INTEIRO','instrucao',3,'p_instrucao_arg2','registos.py',314),
  ('instrucao -> STORE_ARG INTEIRO INTEIRO','instrucao',3,'p_instrucao_arg2','registos.py',315),
  ('instrucao -> CALL INTEIRO IDENTIFICADOR','instrucao',3,'p_instrucao_arg2','registos.py',316),
  ('instrucao -> LOCALS INTEIRO INTEIRO','instrucao',3,'p_instrucao_arg2','registos.py',317),
]
