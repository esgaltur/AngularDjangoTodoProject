import json

#  JsonModel DRF <-> Angular
#
#
class TodoJsonModel:
    id=0
    description=''
    targetDate =None
    IsDone=None
    def __init__(self,id,description,targetDate,IsDone):
          self.id = id
          self.description = description
          self.targetDate = targetDate
          self.IsDone = IsDone

    def to_json(self):
        return json.dumps(self,
                          sort_keys=True, indent=4)