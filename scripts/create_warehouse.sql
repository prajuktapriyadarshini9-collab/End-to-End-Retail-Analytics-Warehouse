create or replace warehouse compute_wh
with
warehouse_size = 'XSMALL'
auto_suspend = 60
auto_resume = True
initially_suspended = TRUE;