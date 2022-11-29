from botocore.exceptions import ClientError
import time

import boto3

import logging as log



# taking the input from user where want to create internet gateway 
REGION= input("Please, Enter the region name where you want to Delete this NACL:- ")

client = boto3.client("ec2", region_name=REGION)

# setup the logger config
logger_info = log.getLogger()
log.basicConfig(level=log.INFO,format=' %(message)s')

# function to detach the internet gateway to the VPC
def detach(gateway_id, vpc_id):

    try:
        response = client.detach_internet_gateway(

            GatewayId=gateway_id, VpcId=vpc_id
            )

    except ClientError:

        logger_info.exception('Sorry, Not able to detach the internet gateway from given VPC')
        raise

    else:
        return response


if __name__ == '__main__':
    
    # taking internet gateway id from user
    GATEWAY_ID = input("Please enter the internet gateway ID:-  ")

    # taking the VPC ID from user where the internet gateway is created

    VPC_ID = input("Please enter the VPC ID to detach the internet gateway:- ")

    for i in range(3):

        logger_info.info('detaching an internet gateway to the VPC...')
        logger_info.info(f'Please wait ......  \n We are detaching  your internet gateway to the VPC....\U0001F570')

        time.sleep(3)     

    gateway = detach(GATEWAY_ID, VPC_ID)
    logger_info.info(f'\nHurry, Your Internet gateway {GATEWAY_ID} has been detahced from the VPC {VPC_ID} successfully \U0001F44D ')