#!/usr/bin/env python
# coding: utf-8


#import important libraries
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import style
import numpy as np 
import seaborn as sns 


# ### Implement a Function Which return Original DataFrame, Transposed DataFrames
''' 
    function with a docstring reading the dataframe, transposing it and 
    populating the header with header information 
    from the dataframe 
'''
def worldbank_data_transpose(filename: str):
    ''' 
        this function transpose data
    '''
    # Read the file into a pandas dataframe
    dataframe = pd.read_csv(filename,skiprows=1)
    
    # Transpose the dataframe
    df_transposed = dataframe.transpose()
    
    # Populate the header of the transposed dataframe with the header information 
   
    # silice the dataframe to get the year as columns
    df_transposed.columns = df_transposed.iloc[1]
    # As year is now columns so we don't need it as rows
    df_transposed_year = df_transposed[0:].drop('year')
    
    # silice the dataframe to get the country as columns
    df_transposed.columns = df_transposed.iloc[0]
    
    # As country is now columns so we don't need it as rows
    df_transposed_country = df_transposed[0:].drop('country')
    
    return dataframe, df_transposed_country, df_transposed_year




def bargraph():
    ''' 
        function will show bar graph
    '''
    # Passing filename to worldbank_data_transpose function 
    orig_df, country_as_col, year_as_col = worldbank_data_transpose('wb_cc_dataset.csv')
    # ### Create DataFrame related to Forest Area Data
    # ### For All the countries and years
    # we want to see countries argricultural land over specfic years
    # we need to filter our original data frame to get specific fields
    arg_land_data = orig_df[['country','year','agricultural_land']]

    # drop the null values present in the dataset
    arg_land_data = arg_land_data.dropna()


    # ### Get Data to Specific Years from 1990 to 2020

    # data related to 1990 
    arg_land_data_1990 = arg_land_data[arg_land_data['year'] == 1990] 

    # data related to 1995
    arg_land_data_1995 = arg_land_data[arg_land_data['year'] == 1995] 

    # data related to 2000
    arg_land_data_2000 = arg_land_data[arg_land_data['year'] == 2000] 

    # data related to 2005 
    arg_land_data_2005 = arg_land_data[arg_land_data['year'] == 2005] 

    # data related to 2010 
    arg_land_data_2010 = arg_land_data[arg_land_data['year'] == 2010]

    # data related to 2015 
    arg_land_data_2015 = arg_land_data[arg_land_data['year'] == 2015]

    # data related to 2020 
    arg_land_data_2020 = arg_land_data[arg_land_data['year'] == 2020] 


    # ### Plot Barplot

    style.use('ggplot')

    # set fig size
    plt.figure(figsize=(15,10))

    # set width of bars
    barWidth = 0.1

    # plot bar charts
    plt.bar(np.arange(arg_land_data_1990.shape[0]),
            arg_land_data_1990['agricultural_land'],
            color='red', width=barWidth, label='1990')

    plt.bar(np.arange(arg_land_data_1995.shape[0])+0.2,
            arg_land_data_1995['agricultural_land'],
            color='green',width=barWidth, label='1995')

    plt.bar(np.arange(arg_land_data_2000.shape[0])+0.3,
            arg_land_data_2000['agricultural_land'],
            color='blue',width=barWidth, label='2000')

    plt.bar(np.arange(arg_land_data_2005.shape[0])+0.4,
            arg_land_data_2005['agricultural_land'],
            color='yellow',width=barWidth, label='2005')

    plt.bar(np.arange(arg_land_data_2010.shape[0])+0.5,
            arg_land_data_2010['agricultural_land'],
            color='black',width=barWidth, label='2010')

    plt.bar(np.arange(arg_land_data_2015.shape[0])+0.6,
            arg_land_data_2015['agricultural_land'],
            color='pink',width=barWidth, label='2015')

    plt.bar(np.arange(arg_land_data_2020.shape[0])+0.7,
            arg_land_data_2020['agricultural_land'],
            color='silver',width=barWidth, label='2020')



    # show the legends on the plot
    plt.legend()

    # set the x-axis label
    plt.xlabel('Country',fontsize=15)

    # add title to the plot 
    plt.title("Agricultural Land",fontsize=15)

    # add countries names to the 11 groups on the x-axis
    plt.xticks(np.arange(arg_land_data_2015.shape[0])+0.2,
               ('Australia', 'China', 'Italy', 'India', 'Fiji', 'Kenya',
           'Netherlands','Canada', 'Turkiye', 'Ukraine',
           'United States', 'South Africa'),
               fontsize=10,rotation = 45)

    # show the plot
    plt.show()


def barplot1():
    ''' 
        function will show bar graph
    '''
    orig_df, country_as_col, year_as_col = worldbank_data_transpose('wb_cc_dataset.csv')


  
    # we want to see countries cereal_yield over the years
    # we need to filter our original data frame to get specific fields
    cereal_yield_data = orig_df[['country','year','cereal_yield']]

    # drop the null values present in the dataset
    cereal_yield_data  = cereal_yield_data.dropna()



    # ### Filter from specific year from 1990 to 2020


    # data related to 1990
    cy_data_1990 = cereal_yield_data[cereal_yield_data['year'] == 1990]

    # data related to 1995
    cy_data_1995 = cereal_yield_data[cereal_yield_data['year'] == 1995]

    # data related to 2000
    cy_data_2000 = cereal_yield_data[cereal_yield_data['year'] == 2000]

    # data related to 2005
    cy_data_2005 = cereal_yield_data[cereal_yield_data['year'] == 2005] 

    # data related to 2010
    cy_data_2010 = cereal_yield_data[cereal_yield_data['year'] == 2010]

    # data related to 2015 
    cy_data_2015 = cereal_yield_data[cereal_yield_data['year'] == 2015] 

    # data related to 2020
    cy_data_2020 = cereal_yield_data[cereal_yield_data['year'] == 2020]





    # ### PLOT barplot

    style.use('ggplot')

    # set fig size
    plt.figure(figsize=(15,10))

    # set width of bars
    barWidth = 0.1 

    # plot bar charts
    plt.bar(np.arange(cy_data_1990.shape[0]),
            cy_data_1990['cereal_yield'],
            color='brown', width=barWidth, label='1990')

    plt.bar(np.arange(cy_data_1995.shape[0])+0.2,
            cy_data_1995['cereal_yield'],
            color='red',width=barWidth, label='1995')

    plt.bar(np.arange(cy_data_2000.shape[0])+0.3,
            cy_data_2000['cereal_yield'],
            color='green',width=barWidth, label='2000')

    plt.bar(np.arange(cy_data_2005.shape[0])+0.4,
            cy_data_2005['cereal_yield'],
            color='coral',width=barWidth, label='2005')

    plt.bar(np.arange(cy_data_2010.shape[0])+0.5,
            cy_data_2010['cereal_yield'],
            color='red',width=barWidth, label='2010')

    plt.bar(np.arange(cy_data_2015.shape[0])+0.6,
            cy_data_2015['cereal_yield'],
            color='indigo',width=barWidth, label='2015')

    plt.bar(np.arange(cy_data_2020.shape[0])+0.7,
            cy_data_2020['cereal_yield'],
            color='violet',width=barWidth, label='2020')


    # show the legends on the plot
    plt.legend()

    # set the x-axis label
    plt.xlabel('Country',fontsize=15)

    # add title to the plot 
    plt.title("Cereal Yield",fontsize=15)

    # add countries names to the 11 groups on the x-axis
    plt.xticks(np.arange(cy_data_2010.shape[0])+0.2,
               ('Australia', 'China', 'Italy', 'India', 'Fiji', 'Kenya',
           'Netherlands', 'Canafa', 'Turkiye', 'Ukraine',
           'United States', 'South Africa'),
                 fontsize=10,rotation = 45)

    # show the plot
    plt.show()



orig_df, country_as_col, year_as_col = worldbank_data_transpose('wb_cc_dataset.csv')



# making dataframe of Netherlands data from the original dataframe
neth_df = orig_df[orig_df['country'] == 'Netherlands']
neth_df.head(5)


# ### Implement a Function which removes Null values and return clean data


def remove_null_values(feature):
    ''' 
        function will remove null values
    '''
    return np.array(feature.dropna())



def heatmap():
    ''' 
        function will show heatmap
    '''
    # Making dataframe of all the feature in the avaiable in 
    # netherland dataframe passing it to remove null values function 
    # for dropping the null values 
    greenhouse = remove_null_values(neth_df[['greenhouse_gas_emissions']])

    argicultural_land = remove_null_values(neth_df[['agricultural_land']])

    co2 = remove_null_values(neth_df[['co2_emissions']])

    arable_land = remove_null_values(neth_df[['arable_land']])

    irrigated_land = remove_null_values(neth_df[['agricultural_irrigated_land']])

    cereal_yield = remove_null_values(neth_df[['cereal_yield']])

    population = remove_null_values(neth_df[['population_growth']])

    urban_pop = remove_null_values(neth_df[['urban_population']])

    gdp = remove_null_values(neth_df[['GDP']])


    # after removing the null values we will create datafram for netherland data
    neth_data = pd.DataFrame({'GreenHouse Gases': [greenhouse[x][0] for x in range(30)],
                                     'Argicultural_land': [argicultural_land[x][0] for x in range(30)],
                                     'Co2 emission': [co2[x][0] for x in range(30)],
                                     'Arable_land': [arable_land[x][0] for x in range(30)],
                                     'Cereal yield': [cereal_yield[x][0] for x in range(30)],
                                     'Urban_pop': [urban_pop[x][0] for x in range(30)],
                                     'GDP': [gdp[x][0] for x in range(30)],
                                    })




    neth_data.head(5) # call first 5 row 


    # ### Correlation Heatmap of Netherland

    # create correlation matrix
    corr_matrix = neth_data.corr()
    plt.figure(figsize=(8,5))
    # using seaborn library to create heatmap 
    sns.heatmap(corr_matrix, annot=True,cmap="YlGnBu")
    plt.title("Correlation Heatmap of Netherland")
    plt.show()





def heatmap1():
    ''' 
        function will show heatmap for unitedstates
    '''
    # making dataframe of US data
    us_df = orig_df[orig_df['country'] == 'United States']
    us_df.head(5)




    # Making dataframe of all the feature in the avaiable in 
    # US dataframe passing it to remove null values function 
    # for dropping the null values 
    greenhouse = remove_null_values(us_df[['greenhouse_gas_emissions']])

    argicultural_land = remove_null_values(us_df[['agricultural_land']])

    co2 = remove_null_values(us_df[['co2_emissions']])

    arable_land = remove_null_values(us_df[['arable_land']])

    irrigated_land = remove_null_values(us_df[['agricultural_irrigated_land']])

    cereal_yield = remove_null_values(us_df[['cereal_yield']])

    urban_pop = remove_null_values(us_df[['urban_population']])

    gdp = remove_null_values(us_df[['GDP']])


    # after removing the null values we will create datafram for US data
    us_data = pd.DataFrame({'GreenHouse Gases': [greenhouse[x][0] for x in range(24)],
                                     'Argicultural_land': [argicultural_land[x][0] for x in range(24)],
                                     'Co2 emission': [co2[x][0] for x in range(24)],
                                     'Arable_land': [arable_land[x][0] for x in range(24)],
                                     'Cereal yield': [cereal_yield[x][0] for x in range(24)],
                                     'Urban_pop': [urban_pop[x][0] for x in range(24)],
                                     'GDP': [gdp[x][0] for x in range(24)],
                                    })





    # ### Correlation Heatmap of US
    # create correlation matrix
    corr_matrix = us_data.corr()
    plt.figure(figsize=(8,5))
    # using seaborn library to create heatmap 
    sns.heatmap(corr_matrix, annot=True,cmap="Blues")
    plt.title("Correlation Heatmap of US")
    plt.show()



def heatmap2():
    ''' 
        function will show heat map for south africa
    '''
    # making dataframe of SA data from the original dataframe
    sa_df = orig_df[orig_df['country'] == 'South Africa']


    # Making dataframe of all the feature in the avaiable in 
    # SA dataframe passing it to remove null values function 
    # for dropping the null values 
    greenhouse = remove_null_values(sa_df[['greenhouse_gas_emissions']])

    argicultural_land = remove_null_values(sa_df[['agricultural_land']])

    co2 = remove_null_values(sa_df[['co2_emissions']])

    arable_land = remove_null_values(sa_df[['arable_land']])

    irrigated_land = remove_null_values(sa_df[['agricultural_irrigated_land']])

    cereal_yield = remove_null_values(sa_df[['cereal_yield']])

    population = remove_null_values(sa_df[['population_growth']])

    urban_pop = remove_null_values(sa_df[['urban_population']])

    gdp = remove_null_values(sa_df[['GDP']])


    # after removing the null values we will create datafram for SA data
    sa_data = pd.DataFrame({'GreenHouse Gases': [greenhouse[x][0] for x in range(30)],
                                     'Argicultural_land': [argicultural_land[x][0] for x in range(30)],
                                     'Co2 emission': [co2[x][0] for x in range(30)],
                                     'Arable_land': [arable_land[x][0] for x in range(30)],
                                     'Cereal yield': [cereal_yield[x][0] for x in range(30)],
                                     'Urban_pop': [urban_pop[x][0] for x in range(30)],
                                     'GDP': [gdp[x][0] for x in range(30)],
                                    })



    # create correlation matrix
    corr_matrix = sa_data.corr()
    plt.figure(figsize=(8,5))
    # using seaborn library to create heatmap 
    sns.heatmap(corr_matrix, annot=True,cmap="Greens")
    plt.title("Correlation Heatmap of South Africa Data Features")
    plt.show()




def lineplot():
    ''' 
        function will showline plot
    '''
    # we want to see countries Urban Population over the years
    # we need to filter our original data frame to get specific fields
    urban_pop = orig_df[['country','year','urban_population']]

    # drop the null values present in the dataset
    urban_pop = urban_pop.dropna()


    urban_pop.country.unique() # shows the all the countries in country features


    # ### Filter the Data For All the Countries 

    Aus_urb_pop = urban_pop[urban_pop['country'] == 'Australia']
    chn_urb_pop = urban_pop[urban_pop['country']== 'China']
    ger_urb_pop =  urban_pop[urban_pop['country'] == 'Italy'] 
    ind_urb_pop = urban_pop[urban_pop['country'] == 'India'] 
    jap_urb_pop = urban_pop[urban_pop['country'] == 'Fiji'] 
    mex_urb_pop = urban_pop[urban_pop['country'] == 'Kenya'] 
    neth_urb_pop = urban_pop[urban_pop['country'] == 'Netherlands'] 
    rsa_urb_pop = urban_pop[urban_pop['country'] == 'Canada'] 
    turk_urb_pop = urban_pop[urban_pop['country'] == 'Turkiye'] 
    ukr_urb_pop = urban_pop[urban_pop['country'] == 'Ukraine'] 
    us_urb_pop = urban_pop[urban_pop['country'] == 'United States'] 
    sa_urb_pop = urban_pop[urban_pop['country']== 'South Africa'] 



    # set fig size
    plt.figure(figsize=(10,10))

    # set the line plot value on x-axis and y-axis by year
    # and Urban Population respectively
    plt.plot(Aus_urb_pop.year, Aus_urb_pop.urban_population,label='Australia')
    plt.plot(chn_urb_pop.year, chn_urb_pop.urban_population,label='China')
    plt.plot(ger_urb_pop.year, ger_urb_pop.urban_population,label='Italy')
    plt.plot(ind_urb_pop.year, ind_urb_pop.urban_population,label='India')
    plt.plot(jap_urb_pop.year, jap_urb_pop.urban_population,label='Fiji')
    plt.plot(mex_urb_pop.year, mex_urb_pop.urban_population,label='Kenya')
    plt.plot(neth_urb_pop.year, neth_urb_pop.urban_population,label='Netherlands')
    plt.plot(rsa_urb_pop.year, rsa_urb_pop.urban_population,label='Canada')
    plt.plot(turk_urb_pop.year, turk_urb_pop.urban_population,label='Turkiya')
    plt.plot(ukr_urb_pop.year, ukr_urb_pop.urban_population,label='Ukraine')
    plt.plot(us_urb_pop.year, us_urb_pop.urban_population,label='US')
    plt.plot(sa_urb_pop.year, sa_urb_pop.urban_population,label='South Africa')

    #Set the X-axis label and make it bold
    plt.xlabel('Year',fontweight='bold')

    # set the title
    plt.title("Urban Population")

    # show the legends on the plot and place it on suitable position
    plt.legend(bbox_to_anchor=(0.99,0.6),shadow=True)

    #show the line plot
    plt.show()



def lineplot2():
    ''' 
        function will show line plot
    '''
    # we want to see countries CO2 emission over the years
    # filter our original data frame to get specific fields
    co2_emissions = orig_df[['country','year','co2_emissions']]

    # drop the null values present in the dataset
    co2_emissions = co2_emissions.dropna()


    # ### Filter the Data For All the Countries 
    Aus_co2_em = co2_emissions[co2_emissions['country'] == 'Australia']
    chn_co2_em = co2_emissions[co2_emissions['country']== 'China']
    ger_co2_em =  co2_emissions[co2_emissions['country'] == 'Germany'] 
    ind_co2_em = co2_emissions[co2_emissions['country'] == 'India'] 
    jap_co2_em = co2_emissions[co2_emissions['country'] == 'Japan'] 
    mex_co2_em = co2_emissions[co2_emissions['country'] == 'Mexico'] 
    neth_co2_em = co2_emissions[co2_emissions['country'] == 'Netherlands'] 
    rsa_co2_em = co2_emissions[co2_emissions['country'] == 'Russian Federation'] 
    turk_co2_em = co2_emissions[co2_emissions['country'] == 'Turkiye'] 
    ukr_co2_em = co2_emissions[co2_emissions['country'] == 'Ukraine'] 
    us_co2_em = co2_emissions[co2_emissions['country'] == 'United States'] 
    sa_co2_em = co2_emissions[co2_emissions['country']== 'South Africa'] 


    # ### Line Plot of CO2 emission


    # set fig size
    plt.figure(figsize=(10,10))

    # set the line plot value on x-axis and y-axis by year
    # and CO2 emission respectively
    plt.plot(Aus_co2_em.year, Aus_co2_em.co2_emissions,label='Australia')
    plt.plot(chn_co2_em.year, chn_co2_em.co2_emissions,label='China')
    plt.plot(ger_co2_em.year, ger_co2_em.co2_emissions,label='Germany')
    plt.plot(ind_co2_em.year, ind_co2_em.co2_emissions,label='India')
    plt.plot(jap_co2_em.year, jap_co2_em.co2_emissions,label='Japan')
    plt.plot(mex_co2_em.year, mex_co2_em.co2_emissions,label='Mexico')
    plt.plot(neth_co2_em.year, neth_co2_em.co2_emissions,label='Netherlands')
    plt.plot(rsa_co2_em.year, rsa_co2_em.co2_emissions,label='Russia')
    plt.plot(turk_co2_em.year, turk_co2_em.co2_emissions,label='Turkiya')
    plt.plot(ukr_co2_em.year, ukr_co2_em.co2_emissions,label='Ukraine')
    plt.plot(us_co2_em.year, us_co2_em.co2_emissions,label='US')
    plt.plot(sa_co2_em.year, sa_co2_em.co2_emissions,label='South Africa')

    #Set the X-axis label and make it bold
    plt.xlabel('Year',fontweight='bold')

    # set the title
    plt.title("Co2 Emission")

    # show the legends on the plot and place it on suitable position
    plt.legend(bbox_to_anchor=(0.99,0.6),shadow=True)

    #show the line plot
    plt.show()




bargraph()
barplot1()
lineplot()
lineplot2()
heatmap()
heatmap1()
heatmap2()
