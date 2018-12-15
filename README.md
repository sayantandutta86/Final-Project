# 590PR Final_Project
Fork from here to create your final project repository.

Two things are different than all the previous assignments in 590PR regarding the permissions settings:

1. Please KEEP the "All_Students" team to have Read access.  
2. Whenever you choose to, you are welcome to change your Final Project repository to private or to public.  This will enable you to list it in your resume, website, or other portfolio.

DELETE these lines from TEMPLATE up.

# Title: Prediction of a disease outbreak using Monte Carlo Simulation

## Team Member(s): Janki Thakkar, Sayed Shazeb Hussain, Sayantan Dutta

# Monte Carlo Simulation Scenario & Purpose:
Purpose for our project is to find if the disease outbreak will affect the major population or not.

Scenario :
In a situation where there is a report of a disease which had infected number of people, in that scenario it would greatly benefit if we are able to forecast whether outbreaks of infectious disease will be major among a population. Infectious disease outbreaks have a reasonable chance of either fading out at an early stage or, in the absence of intervention, spreading widely within the population.
If major outbreaks were predictable in the earliest stages of an outbreak, reactive control strategies could be implemented, such as vaccination, quarantine, or culling. However, such measures are costly, time-consuming, inconvenient, and potentially reduce support for future interventions, thus it is not feasible to implement them for every outbreak.
If it were possible to predict when fadeout was likely to occur, the need for costly precautionary control strategies could be minimized.
We will conduct simulations of data for given possible conditions of a fatal disease outbreak and explore the possibility of predicting a certain range or limit which might be useful for predicting major outbreaks and introduce intervention at the optimum time thus saving life as well as keeping expensive control strategies minimized.

The program takes three inputs - virus type, population size of the concerned locality and threshold level for intervention.
The program calculates the probability of spread of the disease to red-zone patients and tells the user whether medical intervention is required or not.

For size of n sample, we are performing the monte-carlo simulation to get its mean or true value to determine if that person is in red zone or not after that we keep on increasing the iteration of n untill it reaches steady steady state value.

In simple terms, we are calculating the score of every individual in the sample randomly to see if it's in the redzone. After that, we will do this for all the iterations of n and execute this k number of times or more for the sample to get the mean value. We are calculating the probability for the sample to be the potential major outbreak as defined below

P(outbreak) = numberofpeople in redzone/ sample size 

If P(outbreak) is greater than the Threshold value (provided by user) then intervention is required.

## Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?

We are considering below variables as the uncertain element in our calculations:
1) Time difference between the last known patient and the current patient (Tdif) (Triangular Distribution)

2) Relative Distance (Rd) (Triangular Distribution)

The score for a person decreases as the distance from hospital increases as the probability of spread
decreases with increasing distance.
 
3) Immunity level (based on gender) (Random distribution)

As per historical data of mortality rates from various diseases taken from various health organization sources 
it has been found that in general female have higher immunity compared to male. So female has been given a lower score 
compared to male.

## Hypothesis or hypotheses before running the simulation:
The factors we are considering for our model is not the exhaustive list of the factors.
After research we zeroed in on the mentioned factors as they seemed to have a significant effect in our predictions.


## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

## All Sources Used:
