
  $(document).ready(function() {
  $('#mytable1').dataTable( {
    paging: true,
    ordering: true,
    orderMulti : true,
    pageLength: 101,
    order: [[ 2, 'desc' ], [ 3, 'desc' ], [4,'desc']],
    columnDefs: [
    {
      targets: [ 2 ],
      orderData: [ 2, 3, 4 ]
    },
    {
      targets: [ 3 ],
      orderData: [ 3, 2, 4 ]  //如果第二列进行排序，有相同数据则按照第一列顺序排列
    },
    {
      targets: [ 4 ],
      orderData: [ 4, 3, 2 ]
    },
    {
      targets: [ 0 ],
      orderData: [ 0, 1]
    } ],
     columns: [    { type: "html" },    { type: "html" },    { type: "num" },    { type: "num" }, {type:"num"}  ]
  } );
} );
