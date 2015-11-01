
  $(document).ready(function() {
  $('#mytable1').dataTable( {
    paging: true,
    ordering: true,
    orderMulti : true,
    pageLength: 101,
    order: [[ 2, 'desc' ], [ 3, 'asc' ]],
    columnDefs: [
    { type: "numeric", targets: [3] },
    {
      targets: [ 2 ],
      orderData: [ 2, 3 ]  //如果第一列进行排序，有相同数据则按照第二列顺序排列
    },
    {
      targets: [ 3 ],
      orderData: [ 3, 2 ]  //如果第二列进行排序，有相同数据则按照第一列顺序排列
    },
    {
      targets: [ 0 ],
      orderData: [ 0, 1]  //如果第五列进行排序，有相同数据则按照第一列顺序排列
    } ],
     columns: [    { type: "html" },    { type: "html" },    { type: "num" },    { type: "num" }  ]
  } );
} );
