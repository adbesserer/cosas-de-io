set NODES;
set ARCS within (NODES cross NODES);
param oferta {NODES} >= 0; # inyecciones
param demanda {NODES} >= 0; # extracciones
check: sum {i in NODES}
oferta[i] = sum {j in NODES} demanda[j];
param coste {ARCS} >= 0; # costes de transp.
minimize Total_Coste;
node Nodo {k in NODES}: net_in=demanda[k]-oferta[k];
arc enlace {(i,j) in ARCS} >= 0,
from Nodo[i], to Nodo[j], obj Total_Coste coste[i,j];