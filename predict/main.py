import os
import strategies

class Robot():
  def __init__(self, strategy, ammount):
    SECRET_KEY = os.getenv('secret')
    ACCOUNT = os.getenv('account')
    self.stategy = stategy
    self.ammount = ammount
    if (SECRET_KEY is None and not args.dry):
      raise Exception("SECRET_KEY is not defined in .env")
    elif (ACCOUNT is None and not args.dry):
      raise Exception("ACCOUNT is not defined in .env")  
    __import__(f'strategies.{strategy}', locals(), globals())
    import strategies

  def start():
    bot = getattr(trategies, strategy)
    bot = bot.Bot(dry=args.dry, account=ACCOUNT, secret_key=SECRET_KEY, bet_size_eth=bet_size_eth, min_balance_eth=min_balance_eth)
    bot.run()
