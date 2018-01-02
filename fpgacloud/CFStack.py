class CFStack:
  def __init__(self, stack_name, template_file_name, region='us-west-2'):
    self.stack_name = stack_name
    self.stack_region = region
    self.template_file_name = template_file_name
