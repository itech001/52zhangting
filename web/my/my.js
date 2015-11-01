
  $(document).ready(function() {
  $('#mytable1').dataTable( {
    searching: true,
    paging: true,
    ordering: true,
    orderMulti : true,
    pageLength: 100,
    order: [[ 2, 'desc' ], [ 3, 'desc' ], [4,'desc'], [5,'desc']],
    columnDefs: [
    {
      targets: [ 2 ],
      orderData: [ 2, 3, 4, 5 ]
    },
    {
      targets: [ 3 ],
      orderData: [ 3, 2, 4, 5 ]  //如果第二列进行排序，有相同数据则按照第一列顺序排列
    },
    {
      targets: [ 4 ],
      orderData: [ 4, 2, 3, 5 ]
    },
    {
      targets: [ 5],
      orderData: [ 5, 2, 3, 4 ]
    },
    {
      targets: [ 0 ],
      orderData: [ 0, 1]
    } ],
     columns: [    { type: "html" },    { type: "html" },    { type: "num" },    { type: "num" }, {type:"num"} , {type:"num"} ]
  } );
} );
