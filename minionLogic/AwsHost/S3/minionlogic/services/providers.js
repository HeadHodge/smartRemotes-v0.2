////////////////////////////////////////////
//            providers.js
////////////////////////////////////////////
console.log(`***Load providers service...`);

///////////////////////////////////////////////
var pingServer = async function(serviceOrder) {
///////////////////////////////////////////////
console.log(`***pingServer: `, serviceOrder);

};

///////////////////////////////////////////////
var receivedNotice = async function(notice) {
///////////////////////////////////////////////
console.log(`***receivedNotice: `, notice.SUBJECT);

	await global.services.orderService.completeOrder(notice);
};

//////////////////////////////////////////////////////////
module.exports = {
//////////////////////////////////////////////////////////
    name          : 'providerServices',
	pingServer    : pingServer,
	receivedNotice: receivedNotice,
};