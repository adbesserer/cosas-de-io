#### Acero Jericho ####

set MATERIALS;

param costes {MATERIALS} >= 0; 		# coste de cada unidad de material
param disponibles {MATERIALS} >= 0; # cuanto tenemos de cada mat
param horasMat {MATERIALS} >=0; 	#horas en preparar cada material
param propLim > 0; 					#proporción limite de MAT2 respecto MAT1
param horasDisp >= 0; 				#numero de horas disponibles en la fabrica
param pedido >= 0; 					#numero de libras a producir

subject to libReq: sum {i in MATERIALS} MATERIALS[i] >= pedido;  
subject to time: sum{k in MATERIALS} MATERIALS[k] * horasMat[k] <= horasDisp;

subject to stock: {j in MATERIALS} MATERIALS[j] <= disponibles[j];

subject to prop: MATERIALS[2]/MATERIALS[1] <= propLim;

minimize C: sum {m in MATERIALS} MATERIALS[m]*costes[m];
