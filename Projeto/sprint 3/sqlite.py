import sqlite3

#cria o bd
banco = sqlite3.connect('dispvag.db')

cursor = banco.cursor()

#cria a tabela vagas
""" cursor.execute("CREATE TABLE vagas_frontend (nome text,nomeempresa text,sobre text,area text,salario text,requisitos text,beneficios text)") """
""" cursor.execute("CREATE TABLE vagas_backend (nome text,nomeempresa text,sobre text,area text,salario text,requisitos text,beneficios text)") """
""" cursor.execute("CREATE TABLE vagas_TI (nome text,nomeempresa text,sobre text,area text,salario text,requisitos text,beneficios text)") """
""" cursor.execute("CREATE TABLE vagas_outros (nome text,nomeempresa text,sobre text,area text,salario text,requisitos text,beneficios text)") """

#atribui dados a tabela vagas 
""" cursor.execute("INSERT INTO vagas_frontend VALUES ('Desenvolvedor Front End - React Native','Invita SW','Experiência em Desenvolver APP em React Native.','Especialista em Informática, TI, Telecomunicações - Programador / Desenvolvedor.','Salário a combinar','Ensino Superior.','Ajuda de custo')")
banco.commit() """

""" cursor.execute("INSERT INTO vagas_backend VALUES ('Desenvolvedor Sênior Back-End - São Paulo-SP','B2B Stack','Desenvolver softwares de alta performance. Ser parte essencial do time, visando a evolução do produto. Experiência com banco de dados relacionados e não relacionados (SQL, PostgreSQL, MySQL). Experiência com Docker e kubernetes; Experiência em desenvolver testes unitários, Gitflow e processos ágeis.','Especialista em Informática, TI, Telecomunicações - Programador / Desenvolvedor','Salário a combinar','Ensino Superior. Experiência requerida: Entre 1 e 3 anos.','Nenhum')")
banco.commit()
cursor.execute("INSERT INTO vagas_backend VALUES ('Desenvolvedor Back-End (Node.Js) - 100% Remoto','DISYS TECNOLOGIA DA INFORMACAO','Experiência de 2 anos com desenvolvimento em Node.Js (Javascript, desejável Typescript). Experiência com testes e documentação de API Rest, Async API. Necessário experiência com ferramentas de versionamento de código. Experiência com bancos relacional e não relacionais (ex: MongoDB, Redis, Postgres SQL). Experiência com testes unitários e integração, TDD. Experiência com sustentação de aplicações em produção, monitoria, troubleshooting e análise.','Encarregado em Informática, TI, Telecomunicações - TI','R$ 100,00 a R$ 13.500,00','Ensino Superior.','Assistência médica. Vale-refeição. Vale-transporte. Seguro de Vida. Assistência odontológica')")
banco.commit()
cursor.execute("INSERT INTO vagas_backend VALUES ('Desenvolvedor Back End - .NET - Brasília-DF','EMPRESA CONFIDENCIAL','Nível Superior em TI ou cursando Lógica de programação Desenvolvimento em linguagem VB Net, C, Dot net Banco de dados – SQL Server Ambiente Windows. Desenvolvimento de aplicações ANDROID STUDIO e IOS. Realização de integrações utilizando API rest.','Analista em Informática, TI, Telecomunicações - Programador / Desenvolvedor','Salário a combinar','Ensino Superior.','Assistência médica. Vale-refeição. Vale-transporte. Vale-alimentação. Assistência odontológica')")
banco.commit()
cursor.execute("INSERT INTO vagas_backend VALUES ('Desenvolvedor.Net Full Stack São Paulo - SP','AZIMUTE MED','Atuar no desenvolvimento e manutenção de sistemas backend e frontend .Net e React.JS. de acordo com metodologia e técnicas adequadas, visando atender objetivos estabelecidos quanto à qualidade, custos, prazos e benefícios. Executar as atividades mais simples às mais complexas. Conhecimentos na plataforma MS .NET – versões 4.5+ e Core 2.2+ e C. Conhecimentos em React.JS para desenvolvimento de frontend. Criação e consumo de serviços REST. Experiência em metodologias ágeis, como SCRUM. Ferramentas (JIRA, MS Teams). Consultas e manipulações de dados com SQLServer, ADO.net, Entity Framework. Tecnologias de front end: React.JS, HTML 5, CSS, Windows Forms, Web Forms. SQL Server (Stored Procedures, Views, comandos SQL complexos).','Analista em Informática, TI, Telecomunicações - Programador / Desenvolvedor.','A combinar','Escolaridade Mínima: Ensino Superior. Experiência desejada: Entre 1 e 3 anos. Banco de dados: SQL Server. Programação: HTML, C#, Dot Net. Aplicações de Escritório: Microsoft Excel','Assistência médica')")
banco.commit()
cursor.execute("INSERT INTO vagas_backend VALUES ('Desenvolvedor .NET - Banco De CV','Macher Tecnologia.','Procuramos profissionais motivados, abertos a aprender novas tecnologias, processos e métodos ao mesmo tempo em que implementam soluções best-in-class. Profissionais capazes de compreender um problema e trazer uma solução end-to-end. Candidatos com curso superior (em andamento ou concluído) em Análise de Sistemas / Engenharia da Computação / Processamento de Dados / Tecnólogo ou área relacionada. Candidatos com experiência profissional prévia relevante em desenvolvimento de Software no mercado corporativo.','Especialista em Informática, TI, Telecomunicações - Programador / Desenvolvedor.','Salario a combinar.','Procuramos profissionais motivados, abertos a aprender novas tecnologias, processos e métodos ao mesmo tempo em que implementamDesenvolvimento C / .NET de - ao menos - 1 ano. Conhecimentos em Bancos de Dados SQL (Oracle/SQL-Server/MySQL preferred). Noções de frameworks JavaScript como Angular ou React. Familiaridade nos Sistemas Operacionais Linux / Windows. Entendimento dos conceitos de ciclo de vida de Software (Software Development Life-Cycle). Git. Inglês técnico para leitura de materiais e pesquisa.','Assistência médica. Assistência odontológica. Vale-alimentação')")
banco.commit() """

""" cursor.execute("INSERT INTO vagas_TI VALUES ('Técnico De TI - Suporte Técnico Em TI - São José-SC','NETS TI TECONOLOGIA LTDA','Experiência na área de TI para o suporte. Formatação e instalação de softwares. Suporte ao cliente.','Assistente em Informática, TI, Telecomunicações – TI','R$ 1.560,00 a R$ 2.500,00 (Bruto mensal)','Ensino Médio (2º Grau).','Vale-alimentação. Vale-transporte. Vale-refeição. Veiculo da Empresa. Ajuda de custo. Auxilio Combustivel. Celular Corporativo')")
banco.commit()
cursor.execute("INSERT INTO vagas_TI VALUES ('Estágio - TI','Escapay Consignados LTDA','Suporte de TI. Analise de banco de dados. Conhecimento em Java, JavaScript e Python. Conhecimento em SQL Server e PostgreSQL.','Estagiário em Informática, TI, Telecomunicações - TI','R$ 1.000,00 a R$ 1.500,00 (Bruto mensal)','Ensino Superior.','Nenhum')")
banco.commit()
cursor.execute("INSERT INTO vagas_TI VALUES ('AUXILIAR DE T.I JORDANESIA - CAJAMAR','KADOSH RH.','Suporte diário da rotina de TI.','Auxiliar em Informática, TI, Telecomunicações – TI','R$ 2.000,00','Curso Técnico. Experiência em atendimento helpdesk a usuário. Atendimento na empresa dos clientes e remoto. Saber instalar e configurar sistema operacional Microsoft e Linux. Configuração de rede e aplicativos Windows. Reparo de equipamentos como Computadores, Notebook e Impressoras. Ter organização, boa comunicação e relacionamento interpessoal Muita vontade de aprender. Ter conhecimento com sistema ERP. Ter vivência com HARDWARE e SOFTWARE.','Refeição no local. Vale-transporte')")
banco.commit()
cursor.execute("INSERT INTO vagas_TI VALUES ('Analista Jr De Infraestrutura - Manutenção De Equipamento Eletrônicos','RHF TALENTOS','Manutenção de equipamentos eletrônicos, instalação e testes de equipamentos eletrônicos (switchs, câmeras, controladores de acesso). Conhecimento de sistemas de rede IP, informática.','Analista em Informática, TI, Telecomunicações - Infraestrutura','R$ 2.000,00 a R$ 2.005,00','Habilitação B. Formação mínima de Técnico em eletrônica. Conhecimento de manutenção em laboratório e campo. Desejável conhecimento em equipamentos de controle de acesso, CFTV e rede TCP-IP.','Vale-transporte. Vale-refeição. Assistência médica')")
banco.commit()
cursor.execute("INSERT INTO vagas_TI VALUES ('Assistente Administrativo Programação','NOSSA RH','Realizar atividades para atender a demanda do departamento de segurança do trabalho para compilação de desvios. Atualização da base de dados do safety check tour, indicadores, tqm, suporte nas ações das lups, flashs de segurança, consolidação das auditorias dos 10 mandamentos. Demais atividades administrativas.','Assistente em Informática, TI, Telecomunicações - Programador / Desenvolvedor','R$ 2.000,00 a R$ 2.633,00','Ensino Superior.','Refeição no local')")
banco.commit() """

""" cursor.execute("INSERT INTO vagas_outros VALUES ('Projetista Vendedor - Rio de Janeiro - RJ','Unica Movelaria','O candidato será responsável pela criação, avaliação e manipulação de projetos para atender as necessidades de nossos clientes e de nossas demandas internas. Que goste de trabalhar com mais de um tipo de projeto. Elaborar planos, programas e projetos.','Assistente em Arquitetura, Decoração, Design - Design de Interiores / Decoração','Salário a combinar, com participações no lucro.','Ensino Médio (2º Grau). Experiência mínima de 2 anos na função, com experiência comprovada. Conhecimento e domínio do programa PROMOB. Domínio no Pacote Office. Criatividade. Capacidade de trabalhar em equipe. Capacidade de gestão de tempo. Capacidade de Exposição Oral. Concentração. Raciocínio Lógico.','Participação nos lucros.')")
banco.commit() 
cursor.execute("INSERT INTO vagas_outros VALUES ('Auxiliar De Escritório - Goiânia-GO','JM CAMAROES E PESCADOS LTDA','Saber se comunicar bem. Conhecimento para aplicações Microsoft Word, Microsoft Excel e Microsoft Outlook.','Auxiliar em Administração - Administração Geral','R$ 1.200,00 a R$ 1.500,00','Ensino Médio. Experiência requerida: Entre 1 e 3 anos.','Refeição no local. Vale-transporte')")
banco.commit() 
cursor.execute("INSERT INTO vagas_outros VALUES ('Auxiliar Administrativo - Vila Adelaide Perella - Guarulhos','Prompt Empregos','Auxiliar em toda rotina administrativa do escritório. Conhecimento médio em Excel, experiência em atendimento telefônico, arquivamento.','Auxiliar em Administração - Administração Geral','R$ 1.600,00','Ensino Médio. (2° grau). Experiência requerida: Entre 1 e 3 anos','Vale-transporte')")
banco.commit() 
cursor.execute("INSERT INTO vagas_outros VALUES ('Recepcionista para clinica - São Paulo-SP','Gati Serviços','Conhecimentos em graficos WEB: Paint Shop PRO. Conhecimento para aplicações Microsoft Word e Microsoft Powerpoint.','Auxiliar em Administração - Recepção','R$ 1.200,00 a R$ 1.300,00','Curso Técnico.','Cesta básica. Vale-transporte')")
banco.commit() 
cursor.execute("INSERT INTO vagas_outros VALUES ('Atendente - Florianópolis-SC','Pizza Para Você Ingleses','Atendimento ao telefone, presencialmente e pelo iFood. Disposto a aprender na área.','Operacional em Alimentação / Gastronomia - Atendente / Recepção / Garçom','Salario a Combinar','Ensino Médio.','Refeição no local. Vale-transporte')")
banco.commit() 
 """

#mostra os dados da tabela vagas
""" cursor.execute("SELECT * FROM vagas")
print(cursor.fetchall()) """

