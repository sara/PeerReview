from app import app, engine
import os

if __name__ == '__main__':
  #db.create_all()
  app.run(debug=True, host = os.getenv('IP', '0.0.0.0'), 
      port = int(os.getenv('PORT', 5000)))


