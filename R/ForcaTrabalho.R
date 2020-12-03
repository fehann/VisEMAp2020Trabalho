library(dplyr)
library(tidyr)
library(sidrar)

# Get data - https://sidra.ibge.gov.br/tabela/4092 
ForcaTrabalho <- get_sidra(api = '/t/4092/n1/all/n2/all/n3/all/v/1641/p/all/c629/32385,32386,32387,32446')

# Add unemployed percentage
ForcaTrabalho_wide <- ForcaTrabalho %>%
  select(-'Condição em relação à força de trabalho e condição de ocupação (Código)') %>%
  spread('Condição em relação à força de trabalho e condição de ocupação', Valor) %>%
  mutate(PercentualDesocupapdo = `Força de trabalho - desocupada` / `Força de trabalho`)

# Export data to csv
write.csv(ForcaTrabalho_wide, "C:\\Users\\fhann\\Desktop\\Fernando\\Para Apple\\FGV\\Trabalho final\\01 Dados\\PNAD\\ForcaTrabalho.csv", row.names = FALSE)
