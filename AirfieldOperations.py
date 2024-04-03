from abc import ABC

class Pilot():
    def __init__(self, IsonBoard, PilotWeight, Experience):
        self.IsonBoard = IsonBoard
        self.PilotWeight = PilotWeight
        self.Experience = Experience
        
    def Eject(self):
        if True:
            self.IsonBoard = False
        
    def Board(self):
        if True:
            self.IsonBoard = True
            

class Engine():
    def __init__(self, Type, MaxPower) -> None:
        self.Type = Type
        self.MaxPower = MaxPower
    
    def GetConsumption(self):
        if self.Type.lower() == "General Electric CF6":
            if self.MaxPower <= 313: #maxpower is 313 KN
                consumption = 10 # 10 litre/km
                return consumption
        
        elif self.Type.lower() == "Pratt & Whitney PW4000":
            if self.MaxPower <= 275: #maxpower is 275 KN
                consumption = 8 # 10 litre/km
                return consumption
        
        elif self.Type.lower() == "Rolls-Royce Trent":
            if self.MaxPower <= 431: #maxpower is 431
                consumption = 12 #12 litres/km
                return consumption
        
        else: 
            return "Engine type is unknown to me."
        

class Engines():
    def __init__(self, count):
        self.count = count
        self.engine = Engine("General Electric CF6", MaxPower=300)
        

class Payload():
    def __init__(self, Type, PayloadWeight):
        self.PayloadType = Type
        self.PayloadWeight = PayloadWeight
        
        
class Payloads():
    def __init__(self, payloads):
      #  self.count = len(payloads)
        self.payloads = payloads
        
    def Add(self, payload_item):
        self.payload_item = payload_item
        self.payloads.append(self.payload_item)
        
    def Remove(self, payload_item):
        try:
            self.payload_item = payload_item
            self.payloads.remove(self.payload_item)
            
        except Exception as e:
            return  e
        
    def Item(self, payload_item):
        for i in range(len(self.payloads)):
            item = self.payloads[i].PayloadType
            if item == payload_item:
                print(f"{payload_item} present in Payloads")
        else:
            print(f"{payload_item} is not present")
            

class Wings():
    def __init__(self, WingType, SweptAngle, FlyMode=True):
        self.WingType = WingType
        self.SweptAngle = SweptAngle
        self.FlyMode = FlyMode
        
    def SetFlyMode(self, FlyMode):
        self.FlyMode = FlyMode
    
    def GetFlyMode(self):
        return self.FlyMode
    
    
class Aircraft(ABC):
    def __init__(self, IsFlying, Colour, Type):
        self.IsFlying = IsFlying
        self.Colour = Colour
        self.Type = Type
    
    def GoUp(self):
        self.Position = "Up"
    
    def GoDown(self):
        self.Position = "Down"

    def GetPosition(self):
        return self.Position
    
payload1 = Payload("Courier",  500)
payload2 = Payload("Luggage", 3000)
payload3 = Payload("Oxygen Mask", 10)
    
class Airplane(Aircraft):
    def __init__(self, Pilot, IsFlying, Colour, Type):
        self.Pilot = Pilot
        self.PlaneEngines = Engines(2)
        self.Payloads = Payloads(payloads=[payload1, payload2, payload3])
        self.Wings = Wings("Trapezoidal", 30.3)
        super().__init__(IsFlying, Colour, Type)
    
    def SetRPath(self, RPath):
        self.RPath = RPath
    
    def SetRVel(self, RVel):
        self.RVel = RVel
    
    def GetRPath(self):
        return self.RPath
    
    def GetRVel(self):
        return self.RVel
    
    
class Rotor():
    def __init__(self, RotorType):
        self.RotorType = RotorType
        
        
class Helicoptor(Aircraft): #Helicoptor has only 1 Engine
    def __init__(self, Pilot, IsFlying, Colour, Type):
        self.Pilot = Pilot
        self.Engine = Engine("Turbo Jet", 134) # 134kW       
        self.Payloads = Payloads(payloads=[payload1, payload2])
        self.Rotor = Rotor("Fully Articulated")
        super().__init__(IsFlying, Colour, Type)
        
    def Rotate(self, RotateAngle):
        self.RPath = RotateAngle        
        
    def SetRVel(self, RVel):
        self.RVel = RVel
        
    def GetRPath(self):
        return self.RPath
        
    def GetRVel(self):
        return self.RVel
    
    
class Balloon(Aircraft):
    def __init__(self, Pilot, IsFlying, Colour, Type):
        self.Pilot = Pilot
        self.Payloads = Payloads(payloads=[payload1, payload2])
        super().__init__(IsFlying, Colour, Type)
   

Pilot1 = Pilot(IsonBoard=True, PilotWeight=72, Experience=10)
     
    
class Airfield():
    def __init__(self, Size):
        self.Size = Size
        self.aircraft1 = Airplane(Pilot=Pilot1, IsFlying=True, Colour = "White", Type="General Electric CF6")
        
    def get_aircraft(self):
        self.aircraft1.GoDown()
        print(self.aircraft1.GetPosition())
        
        
class Wind():
    def __init__(self, Direction, Velocity):
        self.Direction = Direction
        self.Velocity = Velocity
        

class AnyObject():
    def __init__(self, Name, Object):
        self.Name = Name
        self.Object = Object
        
        
field = Airfield(4)
engine1 = field.aircraft1.PlaneEngines.engine.Type
print(engine1)