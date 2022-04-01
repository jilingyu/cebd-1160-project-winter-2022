import WS.customer_service as service

def run_server():

    # Run the service as a single thread.
    service.sales_service()


if __name__ == '__main__':
    run_server()

