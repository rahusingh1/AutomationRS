import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)   # create object to print the logs

    filehandler = logging.FileHandler("logfile.log")  # create object where to print
    # used to define the format of logs.
    # asctime is a variable that wrapped in % so asctime executed at run time and print time
    # levelname is the type of log that will be printed like debug or info etc,
    # at run time python check what kind of error message and print the same.
    # we are wrapping it in %() so that it will evaluate at run time
    # and using s  so to be treated as string and easily concatenation will be happened.
    # used message variable so whatever message you have in double quotes will be printed.
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    # format of log that will be printed are as follows
    # 2019-02-17 12:40:14,798 : CRITICAL : <test case name> : Fatal error in payment on step 4, cannot continue.
    # make a connection between formater and filehander so that logger will get the knowledge and connection between them.
    filehandler.setFormatter(formatter)  # now connection established

    logger.addHandler(filehandler)  # create handler what to print

    # set levels - if you set level to debug then you can see all logs in the output else only the last one.
    logger.setLevel(logging.ERROR)

    # hierarchy or order what logger gets defined is debug > info > warning > error > critical
    # so if you put debug line after info then it will skip the debug print logs only after info as per order.
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")

    # Q. Can we just see only error logs
    # A. Yes we can do that if we set level to error then logger will print from that level to next level only.
    # in pytest no matter what you write you have to wrap it under a method